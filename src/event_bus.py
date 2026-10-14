"""Thread-safe publish-subscribe EventBus pattern implementation."""

import threading
from typing import Callable, Dict, List, Any


class EventBus:
    """Thread-safe publish-subscribe event broker."""

    def __init__(self):
        self._listeners: Dict[str, List[Callable[..., Any]]] = {}
        self._lock = threading.Lock()

    def subscribe(self, event_name: str, handler: Callable[..., Any]) -> None:
        """Register an event handler for a topic."""
        with self._lock:
            if event_name not in self._listeners:
                self._listeners[event_name] = []
            if handler not in self._listeners[event_name]:
                self._listeners[event_name].append(handler)

    def unsubscribe(self, event_name: str, handler: Callable[..., Any]) -> bool:
        """Remove a registered event handler."""
        with self._lock:
            if event_name in self._listeners and handler in self._listeners[event_name]:
                self._listeners[event_name].remove(handler)
                return True
            return False

    def publish(self, event_name: str, *args: Any, **kwargs: Any) -> int:
        """Broadcast an event to all subscribers and return count of invoked handlers."""
        with self._lock:
            handlers = list(self._listeners.get(event_name, []))
        for handler in handlers:
            handler(*args, **kwargs)
        return len(handlers)

    def clear(self, event_name: str = None) -> None:
        """Clear handlers for an event topic or all topics."""
        with self._lock:
            if event_name:
                self._listeners.pop(event_name, None)
            else:
                self._listeners.clear()
