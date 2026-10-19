"""
Cron Expression Parser, Evaluator, and Humanizer.
Parses standard 5-part cron expressions: (min, hour, dom, mon, dow).
"""
from typing import Set, Tuple
from datetime import datetime

def parse_cron_field(field_str: str, min_val: int, max_val: int) -> Set[int]:
    """Parse a single cron field into matching integer values."""
    field_str = field_str.strip()
    if not field_str:
        raise ValueError("Empty cron field")
    values = set()
    for part in field_str.split(","):
        part = part.strip()
        if part == "*":
            values.update(range(min_val, max_val + 1))
        elif part.startswith("*/"):
            step = int(part[2:])
            if step <= 0:
                raise ValueError("Step must be > 0")
            values.update(range(min_val, max_val + 1, step))
        elif "-" in part:
            sub = part.split("-")
            if len(sub) != 2:
                raise ValueError(f"Invalid range syntax: {part}")
            start, end = int(sub[0]), int(sub[1])
            if start < min_val or end > max_val or start > end:
                raise ValueError(f"Range {start}-{end} outside bounds [{min_val}, {max_val}]")
            values.update(range(start, end + 1))
        else:
            val = int(part)
            if val < min_val or val > max_val:
                raise ValueError(f"Value {val} outside bounds [{min_val}, {max_val}]")
            values.add(val)
    return values

def parse_cron(expression: str) -> Tuple[Set[int], Set[int], Set[int], Set[int], Set[int]]:
    """Parse a 5-part cron expression into 5 matching sets."""
    parts = expression.strip().split()
    if len(parts) != 5:
        raise ValueError(f"Cron expression must contain 5 fields, got {len(parts)}")
    minutes = parse_cron_field(parts[0], 0, 59)
    hours = parse_cron_field(parts[1], 0, 23)
    doms = parse_cron_field(parts[2], 1, 31)
    months = parse_cron_field(parts[3], 1, 12)
    dows = parse_cron_field(parts[4], 0, 6)
    return minutes, hours, doms, months, dows

def matches_cron(expression: str, dt: datetime) -> bool:
    """Check if a datetime matches a cron expression."""
    minutes, hours, doms, months, dows = parse_cron(expression)
    cron_dow = (dt.weekday() + 1) % 7
    return (
        dt.minute in minutes and
        dt.hour in hours and
        dt.day in doms and
        dt.month in months and
        cron_dow in dows
    )

def explain_cron(expression: str) -> str:
    """Generate a human-readable description for a 5-part cron expression."""
    parts = expression.strip().split()
    if len(parts) != 5:
        raise ValueError("Cron expression must have 5 fields")
    m, h, dom, mon, dow = parts
    desc = []
    if m == "*":
        desc.append("Every minute")
    elif m.startswith("*/"):
        desc.append(f"Every {m[2:]} minutes")
    else:
        desc.append(f"At minute {m}")

    if h != "*":
        if h.startswith("*/"):
            desc.append(f"every {h[2:]} hours")
        else:
            desc.append(f"past hour {h}")

    if dom != "*":
        desc.append(f"on day {dom} of month")
    if mon != "*":
        desc.append(f"in month {mon}")
    if dow != "*":
        desc.append(f"on weekday {dow}")
    return ", ".join(desc)
