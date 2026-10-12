"""Date and time formatting and manipulation utilities."""

from datetime import datetime, timezone


def format_iso(dt: datetime = None) -> str:
    """Format datetime object into standard ISO 8601 UTC string."""
    if dt is None:
        dt = datetime.now(timezone.utc)
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def human_readable_duration(seconds: int) -> str:
    """Convert duration in seconds into a friendly human-readable string."""
    if seconds < 0:
        return "0s"
    if seconds < 60:
        return f"{seconds}s"
    
    minutes = seconds // 60
    rem_seconds = seconds % 60
    if minutes < 60:
        return f"{minutes}m {rem_seconds}s" if rem_seconds else f"{minutes}m"
        
    hours = minutes // 60
    rem_minutes = minutes % 60
    if hours < 24:
        return f"{hours}h {rem_minutes}m" if rem_minutes else f"{hours}h"
        
    days = hours // 24
    rem_hours = hours % 24
    return f"{days}d {rem_hours}h" if rem_hours else f"{days}d"


def days_between(date_str_1: str, date_str_2: str, fmt: str = "%Y-%m-%d") -> int:
    """Calculate absolute days between two date strings."""
    d1 = datetime.strptime(date_str_1, fmt)
    d2 = datetime.strptime(date_str_2, fmt)
    return abs((d2 - d1).days)


def is_leap_year(year: int) -> bool:
    """Determine whether a given calendar year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
