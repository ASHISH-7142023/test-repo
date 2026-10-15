"""URL query parameter parsing, sanitization, and serialization helpers."""

import urllib.parse
from typing import Any, Dict, List, Optional


def parse_query_params(query_str: str) -> Dict[str, Any]:
    """Parse query string into dictionary, collapsing single-item lists."""
    if not query_str:
        return {}
    if query_str.startswith("?"):
        query_str = query_str[1:]
    parsed = urllib.parse.parse_qs(query_str, keep_blank_values=True)
    result = {}
    for k, v in parsed.items():
        result[k] = v[0] if len(v) == 1 else v
    return result


def build_query_string(params: Dict[str, Any], sort_keys: bool = True) -> str:
    """Build normalized URL query string from dictionary."""
    if not params:
        return ""
    filtered = {k: v for k, v in params.items() if v is not None}
    items = sorted(filtered.items()) if sort_keys else list(filtered.items())
    return urllib.parse.urlencode(items, doseq=True)


def filter_query_params(query_str: str, allowed_keys: List[str]) -> str:
    """Strip any query parameters not explicitly present in allowed_keys."""
    params = parse_query_params(query_str)
    retained = {k: v for k, v in params.items() if k in allowed_keys}
    return build_query_string(retained)
