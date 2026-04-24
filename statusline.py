import sys, json
from datetime import datetime, timezone

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

parts = []

ctx = data.get("context_window", {}).get("used_percentage")
if ctx is not None:
    parts.append(f"Ctx: {round(ctx)}%")

rl = data.get("rate_limits", {})

five = rl.get("five_hour", {})
five_pct = five.get("used_percentage")
five_reset = five.get("resets_at")
if five_pct is not None and five_reset is not None:
    t = datetime.fromtimestamp(five_reset, tz=timezone.utc).astimezone()
    parts.append(f"{round(five_pct)}% until {t.strftime('%H:%M')}")

week = rl.get("seven_day", {})
week_pct = week.get("used_percentage")
week_reset = week.get("resets_at")
if week_pct is not None and week_reset is not None:
    t = datetime.fromtimestamp(week_reset, tz=timezone.utc).astimezone()
    parts.append(f"{round(week_pct)}% until {t.strftime('%a %H:%M')}")

print(" | ".join(parts))
