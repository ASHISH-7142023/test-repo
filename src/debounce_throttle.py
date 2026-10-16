"""Debounce and throttle function decorators for controlling execution frequency."""

import time
import functools
import threading
from typing import Callable, Any


def debounce(wait_seconds: float) -> Callable:
    """Decorator postponing function execution until wait_seconds elapse without new invocations."""
    def decorator(fn: Callable) -> Callable:
        timer: threading.Timer = None

        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> None:
            nonlocal timer
            if timer is not None:
                timer.cancel()
            timer = threading.Timer(wait_seconds, lambda: fn(*args, **kwargs))
            timer.start()
        return wrapper
    return decorator


def throttle(interval_seconds: float) -> Callable:
    """Decorator ensuring a function runs at most once per interval_seconds."""
    def decorator(fn: Callable) -> Callable:
        last_called = 0.0
        lock = threading.Lock()

        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal last_called
            with lock:
                now = time.time()
                if now - last_called >= interval_seconds:
                    last_called = now
                    return fn(*args, **kwargs)
                return None
        return wrapper
    return decorator
