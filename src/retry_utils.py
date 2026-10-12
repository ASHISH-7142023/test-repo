"""Resilience and exponential backoff retry utilities."""

import time
import functools
from typing import Callable, Type, Tuple, Any


def retry(
    max_attempts: int = 3,
    delay: float = 0.05,
    backoff: float = 2.0,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,)
) -> Callable:
    """Decorator that retries a function with exponential backoff on exceptions."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt == max_attempts:
                        raise last_exception
                    time.sleep(current_delay)
                    current_delay *= backoff
            if last_exception:
                raise last_exception
        return wrapper
    return decorator
