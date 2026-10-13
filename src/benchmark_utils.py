"""Benchmarking and performance profiling utilities."""

import time
import functools
from typing import Callable, Any, Dict, List, Optional


class BenchmarkTimer:
    """Context manager to measure elapsed execution time in seconds and milliseconds."""

    def __init__(self, name: str = "Execution"):
        self.name = name
        self.start_time: float = 0.0
        self.elapsed: float = 0.0

    def __enter__(self) -> "BenchmarkTimer":
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.elapsed = time.perf_counter() - self.start_time

    @property
    def elapsed_ms(self) -> float:
        """Elapsed time in milliseconds."""
        return self.elapsed * 1000.0


def timed(callback: Optional[Callable[[str, float], None]] = None) -> Callable:
    """Decorator to measure execution time of a function."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            t0 = time.perf_counter()
            try:
                return func(*args, **kwargs)
            finally:
                elapsed_sec = time.perf_counter() - t0
                if callback:
                    callback(func.__name__, elapsed_sec)
        return wrapper
    return decorator


def benchmark_function(func: Callable, iterations: int = 10, *args: Any, **kwargs: Any) -> Dict[str, float]:
    """Execute function repeatedly and return statistical metrics in seconds."""
    if iterations <= 0:
        raise ValueError("iterations must be greater than zero.")
    
    durations: List[float] = []
    for _ in range(iterations):
        t0 = time.perf_counter()
        func(*args, **kwargs)
        durations.append(time.perf_counter() - t0)

    total_time = sum(durations)
    return {
        "iterations": float(iterations),
        "total_seconds": round(total_time, 6),
        "mean_seconds": round(total_time / iterations, 6),
        "min_seconds": round(min(durations), 6),
        "max_seconds": round(max(durations), 6)
    }
