"""Coarse brace/quote balance check for the dashboard JS block."""
import re

src = open('app/static/dashboard/index.html', encoding='utf-8').read()
m = re.search(r'<script>(.+?)</script>', src, re.S)
js = m.group(1)

depth = 0
max_depth = 0
in_s = in_d = in_b = False
esc = False
in_block = in_line = False

i = 0
while i < len(js):
    ch = js[i]
    if in_line:
        if ch == '\n':
            in_line = False
        i += 1
        continue
    if in_block:
        if ch == '*' and i + 1 < len(js) and js[i + 1] == '/':
            in_block = False
            i += 2
            continue
        i += 1
        continue
    if in_s or in_d or in_b:
        if esc:
            esc = False
            i += 1
            continue
        if ch == '\\':
            esc = True
            i += 1
            continue
        if in_s and ch == "'":
            in_s = False
        elif in_d and ch == '"':
            in_d = False
        elif in_b and ch == '`':
            in_b = False
        i += 1
        continue
    if ch == '/' and i + 1 < len(js):
        nxt = js[i + 1]
        if nxt == '/':
            in_line = True
            i += 2
            continue
        if nxt == '*':
            in_block = True
            i += 2
            continue
    if ch == "'":
        in_s = True
    elif ch == '"':
        in_d = True
    elif ch == '`':
        in_b = True
    elif ch == '{':
        depth += 1
        if depth > max_depth:
            max_depth = depth
    elif ch == '}':
        depth -= 1
    i += 1

print('final brace depth:', depth, '(expect 0)')
print('max nesting:', max_depth)
print('total js chars:', len(js))
