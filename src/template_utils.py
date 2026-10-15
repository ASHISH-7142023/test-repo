"""Lightweight mustache-style string template interpolation engine."""

import re
from typing import Any, Dict

_TOKEN_REGEX = re.compile(r"\{\{\s*([a-zA-Z0-9_.-]+)\s*\}\}")


def render_template(template: str, context: Dict[str, Any], default: str = "") -> str:
    """Render template replacing {{key}} tokens with values from context dictionary."""
    if not template:
        return ""

    def replace_token(match: re.Match) -> str:
        key = match.group(1).strip()
        val = context.get(key)
        if val is None:
            return default
        return str(val)

    return _TOKEN_REGEX.sub(replace_token, template)
