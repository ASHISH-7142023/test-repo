"""Offset and cursor-based pagination calculation helpers."""

import math
from typing import Any, Dict, List, Optional, Sequence, TypeVar

T = TypeVar("T")


class Page:
    """Represents a single paginated slice of items with metadata."""

    def __init__(self, items: List[Any], page: int, per_page: int, total_items: int):
        self.items = items
        self.page = page
        self.per_page = per_page
        self.total_items = total_items
        self.total_pages = max(1, math.ceil(total_items / per_page)) if per_page > 0 else 1
        self.has_next = self.page < self.total_pages
        self.has_prev = self.page > 1

    def to_dict(self) -> Dict[str, Any]:
        return {
            "items": self.items,
            "page": self.page,
            "per_page": self.per_page,
            "total_items": self.total_items,
            "total_pages": self.total_pages,
            "has_next": self.has_next,
            "has_prev": self.has_prev,
        }


def paginate_list(items: Sequence[T], page: int = 1, per_page: int = 10) -> Page:
    """Slice a sequence into a Page object with boundary checks."""
    if page < 1:
        page = 1
    if per_page < 1:
        per_page = 10

    total = len(items)
    start = (page - 1) * per_page
    end = start + per_page
    sliced = list(items[start:end])
    return Page(sliced, page, per_page, total)


def cursor_paginate(items: List[Dict[str, Any]], cursor_key: str, cursor_val: Optional[Any] = None, limit: int = 10) -> Dict[str, Any]:
    """Cursor-based pagination across dictionaries sorted by cursor_key."""
    if cursor_val is None:
        sliced = items[:limit]
    else:
        start_idx = 0
        for i, item in enumerate(items):
            if item.get(cursor_key) == cursor_val:
                start_idx = i + 1
                break
        sliced = items[start_idx:start_idx + limit]

    next_cursor = sliced[-1].get(cursor_key) if len(sliced) == limit else None
    return {
        "items": sliced,
        "limit": limit,
        "next_cursor": next_cursor,
        "has_more": next_cursor is not None,
    }
