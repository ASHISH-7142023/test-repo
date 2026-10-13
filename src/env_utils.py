"""Environment variable parser with type coercion and default fallbacks."""

import os
from typing import Any, List, Optional, Type, TypeVar

T = TypeVar("T")


def get_env_str(key: str, default: str = "") -> str:
    """Retrieve string environment variable or return default."""
    return os.environ.get(key, default)


def get_env_bool(key: str, default: bool = False) -> bool:
    """Retrieve boolean environment variable recognizing common truthy strings."""
    val = os.environ.get(key)
    if val is None:
        return default
    return val.strip().lower() in ("true", "1", "yes", "on", "t", "y")


def get_env_int(key: str, default: int = 0) -> int:
    """Retrieve integer environment variable with fallback."""
    val = os.environ.get(key)
    if val is None:
        return default
    try:
        return int(val.strip())
    except ValueError:
        return default


def get_env_float(key: str, default: float = 0.0) -> float:
    """Retrieve float environment variable with fallback."""
    val = os.environ.get(key)
    if val is None:
        return default
    try:
        return float(val.strip())
    except ValueError:
        return default


def get_env_list(key: str, default: Optional[List[str]] = None, sep: str = ",") -> List[str]:
    """Retrieve list of strings from delimited environment variable."""
    if default is None:
        default = []
    val = os.environ.get(key)
    if val is None:
        return default
    return [item.strip() for item in val.split(sep) if item.strip()]


def require_env(key: str) -> str:
    """Retrieve required environment variable or raise KeyError."""
    val = os.environ.get(key)
    if val is None:
        raise KeyError(f"Missing mandatory environment variable: '{key}'")
    return val
