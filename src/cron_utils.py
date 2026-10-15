"""Lightweight cron expression (5 fields: min hour dom month dow) validator and matcher."""

import re
from typing import Set


def parse_cron_field(field: str, min_val: int, max_val: int) -> Set[int]:
    """Expand a cron field string (*, */5, 1-5, 2,4,6) into a set of matching integers."""
    field = field.strip()
    if field == "*":
        return set(range(min_val, max_val + 1))

    values: Set[int] = set()
    for part in field.split(","):
        if "/" in part:
            subparts = part.split("/")
            base = range(min_val, max_val + 1) if subparts[0] == "*" else range(int(subparts[0]), max_val + 1)
            step = int(subparts[1])
            values.update(x for x in base if (x - min_val) % step == 0)
        elif "-" in part:
            start, end = part.split("-")
            values.update(range(int(start), int(end) + 1))
        else:
            values.add(int(part))
    return {v for v in values if min_val <= v <= max_val}


def matches_cron(cron_expr: str, minute: int, hour: int, day: int, month: int, day_of_week: int) -> bool:
    """Test whether specific datetime components match 5-field cron string."""
    fields = cron_expr.strip().split()
    if len(fields) != 5:
        raise ValueError("Cron expression must have exactly 5 fields.")

    valid_mins = parse_cron_field(fields[0], 0, 59)
    valid_hours = parse_cron_field(fields[1], 0, 23)
    valid_dom = parse_cron_field(fields[2], 1, 31)
    valid_month = parse_cron_field(fields[3], 1, 12)
    valid_dow = parse_cron_field(fields[4], 0, 6)

    return (minute in valid_mins and
            hour in valid_hours and
            day in valid_dom and
            month in valid_month and
            day_of_week in valid_dow)
