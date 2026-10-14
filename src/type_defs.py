"""Common custom type aliases, generic protocols, and runtime type definitions."""

from typing import Any, Callable, Dict, List, Union, Optional, Protocol, runtime_checkable

# Primitive JSON-compatible types
JSONPrimitive = Union[str, int, float, bool, None]
JSONType = Union[JSONPrimitive, Dict[str, Any], List[Any]]

# Numeric types
Number = Union[int, float]

# Common functional types
Predicate = Callable[[Any], bool]
Transformer = Callable[[Any], Any]
Callback = Callable[..., None]


@runtime_checkable
class Serializable(Protocol):
    """Protocol for objects that can be serialized to a dictionary."""

    def to_dict(self) -> Dict[str, Any]:
        ...


@runtime_checkable
class Deserializable(Protocol):
    """Protocol for objects that can be constructed from a dictionary."""

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> Any:
        ...
