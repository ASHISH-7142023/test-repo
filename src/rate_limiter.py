"""Token Bucket rate limiter for API rate limiting and traffic shaping."""

import time
import threading
from typing import Optional


class TokenBucketRateLimiter:
    """
    Thread-safe token bucket rate limiter.
    
    :param rate: Refill rate in tokens per second.
    :param capacity: Maximum burst token capacity.
    """

    def __init__(self, rate: float, capacity: float):
        if rate <= 0 or capacity <= 0:
            raise ValueError("Rate and capacity must be positive numbers.")
        self.rate = float(rate)
        self.capacity = float(capacity)
        self.tokens = float(capacity)
        self.last_refill = time.time()
        self._lock = threading.Lock()

    def _refill(self, now: float) -> None:
        elapsed = now - self.last_refill
        if elapsed > 0:
            self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
            self.last_refill = now

    def allow(self, tokens: float = 1.0) -> bool:
        """Check if request with specified tokens is allowed without blocking."""
        now = time.time()
        with self._lock:
            self._refill(now)
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

    def acquire(self, tokens: float = 1.0, timeout: Optional[float] = None) -> bool:
        """Block until tokens are available or timeout expires."""
        start_time = time.time()
        while True:
            now = time.time()
            with self._lock:
                self._refill(now)
                if self.tokens >= tokens:
                    self.tokens -= tokens
                    return True
                
                needed = tokens - self.tokens
                wait_time = needed / self.rate

            if timeout is not None:
                remaining_timeout = timeout - (time.time() - start_time)
                if remaining_timeout <= 0:
                    return False
                wait_time = min(wait_time, remaining_timeout)

            time.sleep(max(0.001, wait_time))
