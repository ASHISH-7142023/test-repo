"""Collection, list, and dictionary manipulation helpers."""

from typing import List, Dict, Any, TypeVar, Iterable

T = TypeVar("T")


def chunk_list(items: List[T], chunk_size: int) -> List[List[T]]:
    """Split a list into smaller chunks of given maximum size."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def dedupe(items: Iterable[T]) -> List[T]:
    """Remove duplicate items while preserving original occurrence order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def flatten_dict(nested_dict: Dict[str, Any], parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Flatten a nested dictionary into dot-notated key-value pairs."""
    items = []
    for k, v in nested_dict.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def deep_merge(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively merge two dictionaries, with dict2 values taking precedence."""
    result = dict(dict1)
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result
