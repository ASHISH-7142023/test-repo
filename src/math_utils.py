"""Mathematical and statistical utility calculations."""

import math
from typing import List, Union


def clamp(val: Union[int, float], min_val: Union[int, float], max_val: Union[int, float]) -> Union[int, float]:
    """Constrain a numeric value within inclusive bounds."""
    return max(min_val, min(val, max_val))


def percent_change(initial: float, final: float) -> float:
    """Calculate percentage change from initial to final value."""
    if initial == 0:
        raise ValueError("Initial value cannot be zero for percent change calculation.")
    return round(((final - initial) / abs(initial)) * 100, 4)


def moving_average(data: List[float], window_size: int) -> List[float]:
    """Compute simple moving average over a sliding window."""
    if not data or window_size <= 0 or window_size > len(data):
        return []
    
    averages = []
    current_sum = sum(data[:window_size])
    averages.append(round(current_sum / window_size, 4))
    
    for i in range(window_size, len(data)):
        current_sum += data[i] - data[i - window_size]
        averages.append(round(current_sum / window_size, 4))
        
    return averages


def standard_deviation(data: List[float], sample: bool = True) -> float:
    """Calculate population or sample standard deviation."""
    n = len(data)
    if n < 2:
        return 0.0
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1 if sample else n)
    return round(math.sqrt(variance), 4)
