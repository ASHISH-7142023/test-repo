"""Cron next run time calculator for 5-part cron expressions."""

from datetime import datetime, timedelta
from typing import Optional
from src.cron_utils import matches_cron


def get_next_cron_run(
    cron_expr: str,
    after_dt: Optional[datetime] = None,
    max_days: int = 366,
) -> datetime:
    """Find the next occurrence matching the cron expression after a given datetime."""
    if after_dt is None:
        after_dt = datetime.now()

    curr = after_dt.replace(second=0, microsecond=0) + timedelta(minutes=1)
    limit = curr + timedelta(days=max_days)

    while curr < limit:
        dow = curr.isoweekday() % 7
        if matches_cron(cron_expr, curr.minute, curr.hour, curr.day, curr.month, dow):
            return curr
        curr += timedelta(minutes=1)

    raise ValueError(f"No execution found for '{cron_expr}' within {max_days} days.")
