"""Lightweight Finite State Machine (FSM) engine with validated transitions."""

from typing import Dict, Tuple, Optional, Any, Callable


class StateMachine:
    """Deterministic finite state machine with transition event triggers."""

    def __init__(self, initial_state: str):
        self.current_state = initial_state
        # Key: (from_state, event) -> to_state
        self._transitions: Dict[Tuple[str, str], str] = {}
        # Key: (from_state, to_state) -> callback
        self._callbacks: Dict[Tuple[str, str], Callable[[], None]] = {}

    def add_transition(self, from_state: str, event: str, to_state: str, callback: Optional[Callable[[], None]] = None) -> None:
        """Register valid transition from state to state on trigger event."""
        self._transitions[(from_state, event)] = to_state
        if callback:
            self._callbacks[(from_state, to_state)] = callback

    def trigger(self, event: str) -> str:
        """Trigger transition event and return new state."""
        key = (self.current_state, event)
        if key not in self._transitions:
            raise ValueError(f"Invalid transition: event '{event}' from state '{self.current_state}'.")
        next_state = self._transitions[key]
        cb = self._callbacks.get((self.current_state, next_state))
        if cb:
            cb()
        self.current_state = next_state
        return self.current_state
