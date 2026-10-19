"""
RFC 6901 JSON Pointer implementation.
Allows navigating and mutating nested structures using URI-like pointers.
"""
from typing import Any, List

def escape_json_pointer_token(token: str) -> str:
    """Escape '~' to '~0' and '/' to '~1'."""
    return token.replace("~", "~0").replace("/", "~1")

def unescape_json_pointer_token(token: str) -> str:
    """Unescape '~1' to '/' and '~0' to '~'."""
    return token.replace("~1", "/").replace("~0", "~")

def split_json_pointer(pointer: str) -> List[str]:
    """Split pointer string into unescaped path tokens."""
    if pointer == "":
        return []
    if not pointer.startswith("/"):
        raise ValueError("JSON Pointer must start with '/' or be empty")
    tokens = pointer[1:].split("/")
    return [unescape_json_pointer_token(t) for t in tokens]

def resolve_json_pointer(doc: Any, pointer: str, default: Any = None) -> Any:
    """
    Resolve value in doc addressed by RFC 6901 JSON Pointer.
    """
    tokens = split_json_pointer(pointer)
    curr = doc
    for token in tokens:
        if isinstance(curr, dict):
            if token in curr:
                curr = curr[token]
            else:
                return default
        elif isinstance(curr, list):
            if not token.isdigit():
                return default
            idx = int(token)
            if 0 <= idx < len(curr):
                curr = curr[idx]
            else:
                return default
        else:
            return default
    return curr

def set_json_pointer(doc: Any, pointer: str, value: Any) -> Any:
    """
    Set a value at the JSON Pointer path, mutating dicts/lists in-place.
    Returns doc.
    """
    tokens = split_json_pointer(pointer)
    if not tokens:
        return value
    curr = doc
    for token in tokens[:-1]:
        if isinstance(curr, dict):
            if token not in curr:
                curr[token] = {}
            curr = curr[token]
        elif isinstance(curr, list):
            idx = int(token)
            curr = curr[idx]
    last = tokens[-1]
    if isinstance(curr, dict):
        curr[last] = value
    elif isinstance(curr, list):
        idx = int(last)
        if idx == len(curr):
            curr.append(value)
        else:
            curr[idx] = value
    return doc
