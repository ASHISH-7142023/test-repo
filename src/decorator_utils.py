"""General purpose functional decorators: memoization, deprecation warnings, and call timers."""

import functools
import warnings
from typing import Callable, Any, Dict


def memoize(func: Callable) -> Callable:
    """Thread-safe memoization cache for pure deterministic functions."""
    cache: Dict[Any, Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    wrapper.cache = cache
    wrapper.clear_cache = cache.clear
    return wrapper


def deprecated(reason: str = "") -> Callable:
    """Decorator to mark functions or classes as deprecated with warning."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            msg = f"Call to deprecated function '{func.__name__}'."
            if reason:
                msg += f" Reason: {reason}"
            warnings.warn(msg, category=DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def once(func: Callable) -> Callable:
    """Decorator ensuring a function executes only once; subsequent calls return first result."""
    executed = False
    result: Any = None

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        nonlocal executed, result
        if not executed:
            result = func(*args, **kwargs)
            executed = True
        return result
    return wrapper
