"""Lightweight structured JSON and console logger."""

import json
import time
from typing import Any, Dict, Optional
from src.color_utils import colorize, RED, GREEN, YELLOW, CYAN, DIM


class LogLevel:
    DEBUG = 10
    INFO = 20
    WARN = 30
    ERROR = 40


_LEVEL_NAMES = {
    LogLevel.DEBUG: "DEBUG",
    LogLevel.INFO: "INFO",
    LogLevel.WARN: "WARN",
    LogLevel.ERROR: "ERROR",
}

_LEVEL_COLORS = {
    LogLevel.DEBUG: DIM,
    LogLevel.INFO: CYAN,
    LogLevel.WARN: YELLOW,
    LogLevel.ERROR: RED,
}


class DevLogger:
    """Configurable logger with JSON or human-readable colored formatting."""

    def __init__(self, name: str = "app", level: int = LogLevel.INFO, json_format: bool = False):
        self.name = name
        self.level = level
        self.json_format = json_format

    def format_entry(self, level: int, message: str, extra: Optional[Dict[str, Any]] = None) -> str:
        level_name = _LEVEL_NAMES.get(level, "INFO")
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

        if self.json_format:
            entry = {
                "timestamp": timestamp,
                "name": self.name,
                "level": level_name,
                "message": message,
            }
            if extra:
                entry.update(extra)
            return json.dumps(entry)

        color = _LEVEL_COLORS.get(level, "")
        badge = colorize(f"[{level_name}]", color)
        extra_str = f" {extra}" if extra else ""
        return f"{timestamp} {badge} {self.name}: {message}{extra_str}"

    def debug(self, msg: str, **kwargs) -> Optional[str]:
        if self.level <= LogLevel.DEBUG:
            return self.format_entry(LogLevel.DEBUG, msg, kwargs)
        return None

    def info(self, msg: str, **kwargs) -> Optional[str]:
        if self.level <= LogLevel.INFO:
            return self.format_entry(LogLevel.INFO, msg, kwargs)
        return None

    def warn(self, msg: str, **kwargs) -> Optional[str]:
        if self.level <= LogLevel.WARN:
            return self.format_entry(LogLevel.WARN, msg, kwargs)
        return None

    def error(self, msg: str, **kwargs) -> Optional[str]:
        if self.level <= LogLevel.ERROR:
            return self.format_entry(LogLevel.ERROR, msg, kwargs)
        return None
