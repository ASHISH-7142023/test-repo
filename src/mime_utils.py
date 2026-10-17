"""Lightweight zero-dependency MIME type and file extension utilities."""

import os
from typing import Optional, Dict

MIME_TABLE: Dict[str, str] = {
    ".htm": "text/html",
    ".html": "text/html",
    ".css": "text/css",
    ".js": "application/javascript",
    ".mjs": "application/javascript",
    ".json": "application/json",
    ".xml": "application/xml",
    ".txt": "text/plain",
    ".csv": "text/csv",
    ".md": "text/markdown",
    ".markdown": "text/markdown",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
    ".svg": "image/svg+xml",
    ".ico": "image/x-icon",
    ".pdf": "application/pdf",
    ".zip": "application/zip",
    ".tar": "application/x-tar",
    ".gz": "application/gzip",
    ".mp3": "audio/mpeg",
    ".wav": "audio/wav",
    ".mp4": "video/mp4",
    ".webm": "video/webm",
    ".yaml": "application/yaml",
    ".yml": "application/yaml",
    ".toml": "application/toml",
}

EXT_TABLE: Dict[str, str] = {v: k for k, v in MIME_TABLE.items()}


def guess_mime_type(path_or_ext: str, default: str = "application/octet-stream") -> str:
    """Guess MIME type from a file path or extension."""
    ext = os.path.splitext(path_or_ext)[1].lower()
    if not ext and path_or_ext.startswith("."):
        ext = path_or_ext.lower()
    return MIME_TABLE.get(ext, default)


def guess_extension(mime_type: str) -> Optional[str]:
    """Return primary file extension (including dot) for a MIME type."""
    return EXT_TABLE.get(mime_type.strip().lower())


def is_text_mime(mime_type: str) -> bool:
    """Check if MIME type is textual."""
    m = mime_type.lower()
    return m.startswith("text/") or m in {"application/json", "application/xml", "application/yaml", "application/toml"}


def is_image_mime(mime_type: str) -> bool:
    """Check if MIME type is an image."""
    return mime_type.lower().startswith("image/")
