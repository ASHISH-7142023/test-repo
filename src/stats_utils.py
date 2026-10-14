"""Descriptive statistical computations: percentiles, median, mode, and IQR."""

import math
from typing import List, Union, Tuple, Optional


def median(data: List[Union[int, float]]) -> float:
    """Calculate the median (middle value) of a numeric sequence."""
    if not data:
        raise ValueError("Data sequence cannot be empty.")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 1:
        return float(sorted_data[mid])
    return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0


def percentile(data: List[Union[int, float]], p: float) -> float:
    """Calculate the p-th percentile (0 <= p <= 100) using linear interpolation."""
    if not data:
        raise ValueError("Data sequence cannot be empty.")
    if not (0.0 <= p <= 100.0):
        raise ValueError("Percentile p must be between 0 and 100.")
    sorted_data = sorted(data)
    if len(sorted_data) == 1:
        return float(sorted_data[0])
    k = (len(sorted_data) - 1) * (p / 100.0)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return float(sorted_data[int(k)])
    d0 = sorted_data[int(f)] * (c - k)
    d1 = sorted_data[int(c)] * (k - f)
    return float(round(d0 + d1, 6))


def interquartile_range(data: List[Union[int, float]]) -> float:
    """Calculate the Interquartile Range (IQR = Q3 - Q1)."""
    q1 = percentile(data, 25.0)
    q3 = percentile(data, 75.0)
    return round(q3 - q1, 6)


def z_scores(data: List[Union[int, float]]) -> List[float]:
    """Calculate standardized z-scores for each data point."""
    if len(data) < 2:
        return [0.0] * len(data)
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std = math.sqrt(variance)
    if std == 0:
        return [0.0] * len(data)
    return [round((x - mean) / std, 4) for x in data]
