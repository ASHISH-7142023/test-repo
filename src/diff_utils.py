"""Object and dictionary deep comparison and unified text diff utilities."""

import difflib
from typing import Dict, Any, List, Tuple


def diff_dicts(old: Dict[str, Any], new: Dict[str, Any]) -> Dict[str, Any]:
    """
    Compute structured difference between two dictionaries.
    Returns:
      'added': dict of new keys
      'removed': dict of deleted keys
      'modified': dict of {key: (old_val, new_val)}
    """
    added = {k: new[k] for k in new if k not in old}
    removed = {k: old[k] for k in old if k not in new}
    modified = {}
    for k in old:
        if k in new and old[k] != new[k]:
            modified[k] = (old[k], new[k])
    return {
        "added": added,
        "removed": removed,
        "modified": modified
    }


def unified_diff_text(a: str, b: str, fromfile: str = "before", tofile: str = "after") -> str:
    """Generate canonical unified diff string between two text payloads."""
    a_lines = a.splitlines(keepends=True)
    b_lines = b.splitlines(keepends=True)
    diff = difflib.unified_diff(a_lines, b_lines, fromfile=fromfile, tofile=tofile)
    return "".join(diff)
