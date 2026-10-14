"""Pre-compiled regex patterns and text entity extraction helpers."""

import re
from typing import List

_EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
_URL_PATTERN = re.compile(r"https?://(?:www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_+.~#?&/=]*)")
_HASHTAG_PATTERN = re.compile(r"#(\w+)")
_MENTION_PATTERN = re.compile(r"@(\w+)")
_IPV4_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


def extract_emails(text: str) -> List[str]:
    """Find all email addresses within input text."""
    return _EMAIL_PATTERN.findall(text) if text else []


def extract_urls(text: str) -> List[str]:
    """Find all web HTTP/HTTPS URLs within input text."""
    return _URL_PATTERN.findall(text) if text else []


def extract_hashtags(text: str) -> List[str]:
    """Find all hashtag words (without leading '#') in text."""
    return _HASHTAG_PATTERN.findall(text) if text else []


def extract_mentions(text: str) -> List[str]:
    """Find all social mentions (without leading '@') in text."""
    return _MENTION_PATTERN.findall(text) if text else []


def extract_ipv4_addresses(text: str) -> List[str]:
    """Find all potential IPv4 addresses in text."""
    return _IPV4_PATTERN.findall(text) if text else []
