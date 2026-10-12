"""File system and I/O utility helpers."""

import os
import json
import hashlib
import tempfile
from typing import Any, Optional


def ensure_directory(path: str) -> str:
    """Ensure directory exists, creating parent folders if necessary."""
    os.makedirs(path, exist_ok=True)
    return path


def safe_read_json(file_path: str, default: Optional[Any] = None) -> Any:
    """Read JSON file safely without throwing exceptions on missing or corrupt files."""
    if not os.path.exists(file_path):
        return default
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return default


def atomic_write_text(file_path: str, content: str) -> None:
    """Write text atomically using a temporary file to prevent corruption."""
    directory = os.path.dirname(os.path.abspath(file_path))
    ensure_directory(directory)
    
    with tempfile.NamedTemporaryFile("w", dir=directory, delete=False, encoding="utf-8") as tf:
        tf.write(content)
        temp_name = tf.name
        
    os.replace(temp_name, file_path)


def get_file_checksum(file_path: str, algorithm: str = "sha256") -> str:
    """Compute cryptographic hash checksum of a file in streaming chunks."""
    h = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()
