"""Enhanced JSON serialization supporting dates, UUIDs, sets, and custom objects."""

import json
import uuid
from datetime import datetime, date
from typing import Any


class DevToolkitJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder handling datetime, UUID, set, and object serialization."""

    def default(self, obj: Any) -> Any:
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, uuid.UUID):
            return str(obj)
        if isinstance(obj, set):
            return list(obj)
        if hasattr(obj, "to_dict") and callable(obj.to_dict):
            return obj.to_dict()
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        return super().default(obj)


def to_json(obj: Any, indent: int = None) -> str:
    """Serialize object to JSON string using DevToolkitJSONEncoder."""
    return json.dumps(obj, cls=DevToolkitJSONEncoder, indent=indent)


def from_json(json_str: str) -> Any:
    """Deserialize JSON string into native Python objects."""
    return json.loads(json_str)
