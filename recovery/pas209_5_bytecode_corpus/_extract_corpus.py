"""PAS209.5 — Bytecode recovery-corpus extractor.

Preservation tooling ONLY. Stdlib only. Reads source-less *.pyc residue under
app/services/**, app/routes/**, scripts/** and emits durable text artifacts
(docstrings, names, constants, env keys, imports, disassembly) so the lost
PAS160-190 work survives as a *reconstruction specification* even if the stale
__pycache__ bytecode is later cleaned.

This does NOT restore source, does NOT write replacement modules, and does NOT
delete any bytecode. Run from the repo root:  python recovery/pas209_5_bytecode_corpus/_extract_corpus.py
"""
from __future__ import annotations

import dis
import glob
import io
import marshal
import os
import re
import struct
from collections import Counter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CORPUS_DIR = os.path.join(REPO_ROOT, "recovery", "pas209_5_bytecode_corpus")
ROOTS = ["app/services", "app/routes", "scripts"]

# Subsystem grouping for the index. routes/scripts handled specially.
INDEX_ORDER = [
    "ingestion", "memory", "security", "operator", "learning", "monitoring",
    "optimization", "replay", "tenant", "callbacks", "worker", "outbound",
    "brokerage", "simulation", "slack", "routes", "scripts_readiness",
]

# ---- redaction -------------------------------------------------------------
_PEM = re.compile(r"-----BEGIN [A-Z ]+-----")
_FERNET = re.compile(r"^[A-Za-z0-9_\-]{43}=$")               # urlsafe b64, 32 bytes
_LONG_B64 = re.compile(r"^[A-Za-z0-9+/_\-]{40,}={0,2}$")     # high-entropy blob
_HEX = re.compile(r"^[0-9a-fA-F]{40,}$")
_SECRET_HINT = re.compile(r"(secret|password|passwd|private[_-]?key|api[_-]?key|token|bearer)\s*[:=]\s*\S", re.I)
REDACTIONS = 0


def _shannon(s: str) -> float:
    if not s:
        return 0.0
    counts = Counter(s)
    n = len(s)
    import math
    return -sum((c / n) * math.log2(c / n) for c in counts.values())


def redact(s: str):
    """Return (text, was_redacted). Keep identifier-like ENV *names*; redact values."""
    global REDACTIONS
    if _PEM.search(s) or _FERNET.match(s) or _HEX.match(s):
        REDACTIONS += 1
        return f"<REDACTED:secret-like value, len={len(s)}>", True
    if _LONG_B64.match(s) and _shannon(s) > 4.0 and " " not in s:
        REDACTIONS += 1
        return f"<REDACTED:high-entropy blob, len={len(s)}>", True
    if _SECRET_HINT.search(s):
        REDACTIONS += 1
        return "<REDACTED:secret-bearing literal>", True
    return s, False


# ---- pyc loading -----------------------------------------------------------
def load_code(pyc_path: str):
    with open(pyc_path, "rb") as f:
        magic = f.read(4)
        f.read(12)  # 3.7+ header: bitfield(4) + mtime(4) + size(4)
        code = marshal.load(f)
    return magic, code


def walk_codes(code):
    yield code
    for const in code.co_consts:
        if hasattr(const, "co_code"):
            yield from walk_codes(const)


def extract(code):
    module_doc = None
    if code.co_consts and isinstance(code.co_consts[0], str):
        module_doc = code.co_consts[0]

    classes, functions, imports = [], [], set()
    str_consts, env_keys = [], set()

    # top-level instructions: classify functions vs classes via MAKE_FUNCTION /
    # LOAD_BUILD_CLASS, and collect imports across all code objects.
    for c in walk_codes(code):
        for ins in dis.get_instructions(c):
            if ins.opname in ("IMPORT_NAME", "IMPORT_FROM") and isinstance(ins.argval, str):
                imports.add(ins.argval)

    # function/class names from nested code objects
    build_class_consumers = set()
    for ins in dis.get_instructions(code):
        pass
    for const in code.co_consts:
        if hasattr(const, "co_code"):
            name = const.co_name
            # class bodies have co_name == class name and contain __qualname__/__module__
            if "__qualname__" in const.co_names or const.co_name[:1].isupper():
                classes.append(name)
            else:
                functions.append(name)

    # constants (recursively) -> strings + env-key candidates
    seen = set()
    for c in walk_codes(code):
        for k in c.co_consts:
            if isinstance(k, str):
                if k in seen:
                    continue
                seen.add(k)
                if k and (k == k.upper()) and re.match(r"^[A-Z][A-Z0-9_]{2,}$", k):
                    env_keys.add(k)
                if len(k) >= 3 and not k.startswith("__"):
                    str_consts.append(k)

    # de-dup, keep stable order
    classes = sorted(set(classes))
    functions = sorted(set(f for f in functions if f != "<lambda>"))
    return {
        "doc": module_doc,
        "classes": classes,
        "functions": functions,
        "imports": sorted(imports),
        "env_keys": sorted(env_keys),
        "str_consts": str_consts,
    }


def disassembly_text(code) -> str:
    buf = io.StringIO()
    try:
        dis.dis(code, file=buf)
    except Exception as e:  # pragma: no cover - defensive
        buf.write(f"<disassembly failed: {type(e).__name__}: {e}>")
    return buf.getvalue()


def subsystem_of(root: str, srcdir: str) -> str:
    if root == "scripts":
        return "scripts_readiness"
    if root == "app/routes":
        return "routes"
    parts = srcdir.replace("\\", "/").split("/")
    return parts[2] if len(parts) > 2 else "unknown"


def md_escape_block(s: str) -> str:
    return s.replace("\r\n", "\n")


def main():
    sourceless = []
    for root in ROOTS:
        for pyc in glob.glob(os.path.join(REPO_ROOT, root, "**", "__pycache__", "*.pyc"), recursive=True):
            base = os.path.basename(pyc)
            mod = base.split(".cpython")[0]
            srcdir = os.path.dirname(os.path.dirname(pyc))
            if not os.path.exists(os.path.join(srcdir, mod + ".py")):
                rel_srcdir = os.path.relpath(srcdir, REPO_ROOT)
                sourceless.append((root, rel_srcdir, mod, pyc))

    by_sub = {}
    artifact_count = 0
    inspected = 0
    redacted_modules = 0

    for root, rel_srcdir, mod, pyc in sorted(sourceless, key=lambda x: (subsystem_of(x[0], x[1]), x[2])):
        sub = subsystem_of(root, rel_srcdir)
        out_dir = os.path.join(CORPUS_DIR, sub)
        os.makedirs(out_dir, exist_ok=True)
        try:
            magic, code = load_code(pyc)
            info = extract(code)
            disasm = disassembly_text(code)
            inspected += 1
        except Exception as e:
            by_sub.setdefault(sub, []).append((mod, f"LOAD-FAILED: {type(e).__name__}", rel_srcdir))
            with open(os.path.join(out_dir, mod + ".md"), "w", encoding="utf-8") as fh:
                fh.write(f"# {sub}/{mod}\n\nLOAD FAILED: {type(e).__name__}: {e}\n\npyc: `{os.path.relpath(pyc, REPO_ROOT)}`\n")
            artifact_count += 1
            continue

        # redact string constants
        red_strs = []
        any_red = False
        for s in info["str_consts"]:
            t, was = redact(s)
            any_red = any_red or was
            red_strs.append((t, was))
        if any_red:
            redacted_modules += 1

        magic_hex = magic.hex()
        src_path = getattr(code, "co_filename", "")
        doc = (info["doc"] or "").strip()
        doc_first = doc.splitlines()[0] if doc else ""

        by_sub.setdefault(sub, []).append((mod, doc_first, rel_srcdir))

        lines = []
        lines.append(f"# {sub}/{mod}")
        lines.append("")
        lines.append(f"- **pyc:** `{os.path.relpath(pyc, REPO_ROOT)}`")
        lines.append(f"- **expected source path (absent):** `{rel_srcdir}/{mod}.py`")
        lines.append(f"- **co_filename (from bytecode):** `{src_path}`")
        lines.append(f"- **source present:** False")
        lines.append(f"- **python magic:** `{magic_hex}` (CPython 3.14)")
        lines.append(f"- **subsystem:** {sub}")
        lines.append("")
        lines.append("## Module docstring")
        lines.append("")
        lines.append("```\n" + (doc if doc else "<none>") + "\n```")
        lines.append("")
        lines.append("## Imports")
        lines.append("")
        lines.append(", ".join(f"`{i}`" for i in info["imports"]) or "_none discoverable_")
        lines.append("")
        lines.append("## Classes")
        lines.append("")
        lines.append(", ".join(f"`{c}`" for c in info["classes"]) or "_none_")
        lines.append("")
        lines.append("## Functions / methods")
        lines.append("")
        lines.append(", ".join(f"`{fn}`" for fn in info["functions"]) or "_none_")
        lines.append("")
        lines.append("## Env-key candidates")
        lines.append("")
        lines.append(", ".join(f"`{e}`" for e in info["env_keys"]) or "_none_")
        lines.append("")
        lines.append("## String constants (redacted where noted)")
        lines.append("")
        if red_strs:
            for t, was in red_strs:
                prefix = "🔒 " if was else ""
                lines.append(f"- {prefix}{t!r}")
        else:
            lines.append("_none_")
        lines.append("")
        lines.append("## Disassembly")
        lines.append("")
        lines.append("```")
        lines.append(md_escape_block(disasm).rstrip())
        lines.append("```")
        lines.append("")

        with open(os.path.join(out_dir, mod + ".md"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        artifact_count += 1

    # ---- index.md ----
    idx = []
    idx.append("# PAS209.5 Bytecode Recovery Corpus — Index")
    idx.append("")
    idx.append("Durable text artifacts extracted from **source-less** `.pyc` bytecode "
               "(CPython 3.14) — the only surviving residue of the lost PAS160–190 work.")
    idx.append("")
    idx.append("This is a **reconstruction specification, not restored source code.** "
               "No decompilation was performed (no CPython-3.14 decompiler exists); "
               "artifacts are produced via stdlib `marshal` + `dis` only.")
    idx.append("")
    total = sum(len(v) for v in by_sub.values())
    idx.append(f"**Modules captured:** {total}  |  **Redacted modules:** {redacted_modules}  |  **Redactions:** {REDACTIONS}")
    idx.append("")
    idx.append("| Subsystem | Modules |")
    idx.append("|---|---|")
    for sub in INDEX_ORDER:
        if sub in by_sub:
            idx.append(f"| {sub} | {len(by_sub[sub])} |")
    for sub in sorted(by_sub):
        if sub not in INDEX_ORDER:
            idx.append(f"| {sub} | {len(by_sub[sub])} |")
    idx.append(f"| **TOTAL** | **{total}** |")
    idx.append("")

    for sub in INDEX_ORDER + [s for s in sorted(by_sub) if s not in INDEX_ORDER]:
        if sub not in by_sub:
            continue
        idx.append(f"## {sub}")
        idx.append("")
        for mod, doc_first, rel_srcdir in sorted(by_sub[sub]):
            summary = (doc_first or "").strip()
            if len(summary) > 110:
                summary = summary[:107] + "..."
            link = f"{sub}/{mod}.md"
            idx.append(f"- [`{mod}`]({link}) — {summary}" if summary else f"- [`{mod}`]({link})")
        idx.append("")

    with open(os.path.join(CORPUS_DIR, "index.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(idx))

    print(f"inspected={inspected} artifacts={artifact_count} redacted_modules={redacted_modules} redactions={REDACTIONS}")
    for sub in INDEX_ORDER + [s for s in sorted(by_sub) if s not in INDEX_ORDER]:
        if sub in by_sub:
            print(f"  {sub}: {len(by_sub[sub])}")


if __name__ == "__main__":
    main()
