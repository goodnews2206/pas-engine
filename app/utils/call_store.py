"""
Shared in-process stores for call context.

pending_leads  — keyed by phone number, populated by /outbound/call before
                 Twilio dials out. Consumed by /twilio/voice on answer.
active_calls   — keyed by call_sid, live from webhook answer → WebSocket close.
                 Lets the WebSocket handler read lead context set by the webhook.
"""

pending_leads: dict[str, dict] = {}
active_calls: dict[str, dict] = {}
