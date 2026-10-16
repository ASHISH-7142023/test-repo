"""Binary search bounds and element range search helpers."""

from typing import Any, Callable, List, Optional, Tuple


def binary_search(arr: List[Any], target: Any, key: Optional[Callable[[Any], Any]] = None) -> int:
    """Find index of target in sorted array, or return -1 if missing."""
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        val = key(arr[mid]) if key else arr[mid]
        if val == target:
            return mid
        elif val < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search_range(arr: List[Any], target: Any) -> Tuple[int, int]:
    """Find the starting and ending index of a target value in sorted array."""
    def find_bound(is_left: bool) -> int:
        l, r = 0, len(arr) - 1
        bound = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                bound = mid
                if is_left:
                    r = mid - 1
                else:
                    l = mid + 1
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return bound

    return find_bound(True), find_bound(False)
