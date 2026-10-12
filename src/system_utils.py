"""System diagnostics and environment information utilities."""

import os
import shutil
import platform
from typing import Dict, Any


def get_platform_info() -> Dict[str, str]:
    """Retrieve runtime operating system and python platform metadata."""
    return {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": platform.python_version()
    }


def format_bytes(bytes_count: int) -> str:
    """Format raw byte counts into human-readable digital storage units."""
    if bytes_count < 0:
        return "0 B"
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = float(bytes_count)
    unit_index = 0
    while size >= 1024.0 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1
    return f"{size:.2f} {units[unit_index]}"


def get_disk_usage(path: str = ".") -> Dict[str, Any]:
    """Return storage metrics (total, used, free, percent_used) for path."""
    total, used, free = shutil.disk_usage(os.path.abspath(path))
    percent_used = round((used / total) * 100, 2) if total > 0 else 0.0
    return {
        "total_bytes": total,
        "used_bytes": used,
        "free_bytes": free,
        "total_formatted": format_bytes(total),
        "used_formatted": format_bytes(used),
        "free_formatted": format_bytes(free),
        "percent_used": percent_used
    }
