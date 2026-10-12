"""String manipulation and text processing utilities."""

import re
import unicodedata

# Pre-compiled regex patterns for performance
_NON_WORD_PATTERN = re.compile(r"[^\w\s-]")
_DELIMITER_PATTERN = re.compile(r"[\s_-]+")
_CAMEL_TO_SNAKE_1 = re.compile(r"(.)([A-Z][a-z]+)")
_CAMEL_TO_SNAKE_2 = re.compile(r"([a-z0-9])([A-Z])")
_HTML_TAGS_PATTERN = re.compile(r"<[^>]+>")


def slugify(text: str, delimiter: str = "-") -> str:
    """Convert text into an ASCII URL-safe slug."""
    if not text:
        return ""
    # Normalize unicode to ASCII representation
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    # Lowercase and remove non-word characters
    text = _NON_WORD_PATTERN.sub("", text).strip().lower()
    # Replace spaces or repeated delimiters with single delimiter
    return _DELIMITER_PATTERN.sub(delimiter, text)


def camel_to_snake(text: str) -> str:
    """Convert camelCase or PascalCase string to snake_case."""
    if not text:
        return ""
    s1 = _CAMEL_TO_SNAKE_1.sub(r"\1_\2", text)
    return _CAMEL_TO_SNAKE_2.sub(r"\1_\2", s1).lower()


def snake_to_camel(text: str, pascal: bool = False) -> str:
    """Convert snake_case string to camelCase or PascalCase."""
    if not text:
        return ""
    parts = text.split("_")
    if pascal:
        return "".join(p.capitalize() for p in parts)
    return parts[0].lower() + "".join(p.capitalize() for p in parts[1:])


def truncate_words(text: str, max_words: int = 10, suffix: str = "...") -> str:
    """Truncate text to a maximum number of words."""
    if not text:
        return ""
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + suffix


def mask_sensitive(text: str, visible_chars: int = 4, mask_char: str = "*") -> str:
    """Mask sensitive string (e.g. credit card, api key) revealing only trailing characters."""
    if not text:
        return ""
    if len(text) <= visible_chars:
        return text
    masked_part = mask_char * (len(text) - visible_chars)
    visible_part = text[-visible_chars:]
    return f"{masked_part}{visible_part}"


def strip_html_tags(html: str) -> str:
    """Remove HTML/XML tags from markup string."""
    if not html:
        return ""
    return _HTML_TAGS_PATTERN.sub("", html).strip()
