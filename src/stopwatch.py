"""High-precision multi-lap stopwatch with split timing and statistics."""

import time
from typing import Dict, List


class SplitStopwatch:
    """Stopwatch tracking overall elapsed duration and individual lap split intervals."""

    def __init__(self):
        self._start_time: float = 0.0
        self._laps: List[float] = []
        self._last_split: float = 0.0
        self._is_running: bool = False

    def start(self) -> None:
        """Start or restart the stopwatch."""
        self._start_time = time.perf_counter()
        self._last_split = self._start_time
        self._laps = []
        self._is_running = True

    def lap(self) -> float:
        """Record lap duration since last lap call in seconds."""
        if not self._is_running:
            raise RuntimeError("Stopwatch must be started before recording laps.")
        now = time.perf_counter()
        duration = now - self._last_split
        self._laps.append(duration)
        self._last_split = now
        return duration

    def stop(self) -> float:
        """Stop timing and return total elapsed duration."""
        if not self._is_running:
            return sum(self._laps)
        now = time.perf_counter()
        final_lap = now - self._last_split
        self._laps.append(final_lap)
        self._is_running = False
        return now - self._start_time

    def summary(self) -> Dict[str, float]:
        """Return statistical breakdown of laps."""
        if not self._laps:
            return {"laps": 0, "total": 0.0, "avg_lap": 0.0, "fastest": 0.0, "slowest": 0.0}
        return {
            "laps": float(len(self._laps)),
            "total": round(sum(self._laps), 4),
            "avg_lap": round(sum(self._laps) / len(self._laps), 4),
            "fastest": round(min(self._laps), 4),
            "slowest": round(max(self._laps), 4)
        }
