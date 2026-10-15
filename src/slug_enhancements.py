"""Enhanced slugification with stop-words removal and custom delimiter filters."""

import re
from src.string_utils import slugify

_DEFAULT_STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for", "of", "with", "by"
}


def advanced_slugify(text: str, remove_stopwords: bool = True, custom_stopwords: set = None) -> str:
    """Generate SEO-friendly slug optionally removing common English stopwords."""
    if not text:
        return ""
    words = re.findall(r"\w+", text.lower())
    stopwords = custom_stopwords if custom_stopwords is not None else _DEFAULT_STOPWORDS
    if remove_stopwords:
        words = [w for w in words if w not in stopwords]
    return slugify(" ".join(words))
