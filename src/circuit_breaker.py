"""Circuit Breaker resilience pattern for distributed calls and external services."""

import time
import threading
from typing import Callable, Any


class CircuitBreakerOpenException(Exception):
    """Raised when request is denied because circuit is open."""
    pass


class CircuitBreaker:
    """
    Circuit breaker with CLOSED, OPEN, and HALF_OPEN states.
    
    :param failure_threshold: Consecutive failures before tripping open.
    :param recovery_timeout: Seconds to wait before attempting half-open probe.
    """

    STATE_CLOSED = "CLOSED"
    STATE_OPEN = "OPEN"
    STATE_HALF_OPEN = "HALF_OPEN"

    def __init__(self, failure_threshold: int = 3, recovery_timeout: float = 1.0):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.state = self.STATE_CLOSED
        self.failure_count = 0
        self.last_failure_time = 0.0
        self._lock = threading.Lock()

    def call(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        with self._lock:
            now = time.time()
            if self.state == self.STATE_OPEN:
                if now - self.last_failure_time > self.recovery_timeout:
                    self.state = self.STATE_HALF_OPEN
                else:
                    raise CircuitBreakerOpenException("Circuit is open; call rejected.")

        try:
            res = func(*args, **kwargs)
            with self._lock:
                if self.state == self.STATE_HALF_OPEN:
                    self.state = self.STATE_CLOSED
                    self.failure_count = 0
            return res
        except Exception:
            with self._lock:
                self.failure_count += 1
                self.last_failure_time = time.time()
                if self.failure_count >= self.failure_threshold:
                    self.state = self.STATE_OPEN
            raise
