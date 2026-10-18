"""Linear time Radix Sort and Counting Sort implementations."""

from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    """Sort integer list using Counting Sort."""
    if not arr:
        return []
    min_val = min(arr)
    max_val = max(arr)
    counts = [0] * (max_val - min_val + 1)

    for num in arr:
        counts[num - min_val] += 1

    sorted_arr = []
    for offset, cnt in enumerate(counts):
        sorted_arr.extend([offset + min_val] * cnt)
    return sorted_arr


def radix_sort_integers(arr: List[int]) -> List[int]:
    """Sort list of arbitrary integers (including negatives) in O(d * n) time."""
    if not arr:
        return []

    positives = [x for x in arr if x >= 0]
    negatives = [-x for x in arr if x < 0]

    def _lsd_radix(nums: List[int]) -> List[int]:
        if not nums:
            return []
        max_num = max(nums)
        exp = 1
        res = list(nums)

        while max_num // exp > 0:
            buckets: List[List[int]] = [[] for _ in range(10)]
            for num in res:
                digit = (num // exp) % 10
                buckets[digit].append(num)
            res = [num for bucket in buckets for num in bucket]
            exp *= 10
        return res

    sorted_positives = _lsd_radix(positives)
    sorted_negatives = _lsd_radix(negatives)

    return [-x for x in reversed(sorted_negatives)] + sorted_positives
