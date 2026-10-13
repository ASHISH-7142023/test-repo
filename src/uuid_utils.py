"""UUID generation, transformation, and validation helpers."""

import re
import uuid
import base64

_UUID_REGEX = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
    re.IGNORECASE
)


def generate_uuid4() -> str:
    """Generate a standard random UUIDv4 string."""
    return str(uuid.uuid4())


def generate_uuid5(namespace_uuid: str, name: str) -> str:
    """Generate deterministic UUIDv5 using namespace and name string."""
    ns = uuid.UUID(namespace_uuid)
    return str(uuid.uuid5(ns, name))


def is_valid_uuid(val: str) -> bool:
    """Validate whether string matches canonical UUID format."""
    if not val or not isinstance(val, str):
        return False
    return bool(_UUID_REGEX.match(val.strip()))


def short_uuid(u: str = None) -> str:
    """
    Generate or convert existing UUID into a compact 22-character URL-safe string.
    """
    if u is None:
        raw_bytes = uuid.uuid4().bytes
    else:
        raw_bytes = uuid.UUID(u).bytes
    # Base64 url-safe without trailing padding '=='
    return base64.urlsafe_b64encode(raw_bytes).decode("ascii").rstrip("=")


def expand_short_uuid(short_str: str) -> str:
    """Convert 22-character short UUID back into standard 36-char canonical UUID string."""
    padded = short_str + "=="
    raw_bytes = base64.urlsafe_b64decode(padded.encode("ascii"))
    return str(uuid.UUID(bytes=raw_bytes))
