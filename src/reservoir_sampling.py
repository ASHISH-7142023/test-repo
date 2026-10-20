"""
Reservoir Sampling (Algorithm R and Algorithm L).
Uniformly selects k random items from an iterator of unknown or infinite length.
"""
import random
from typing import Iterable, List, TypeVar

T = TypeVar("T")

def reservoir_sample(iterable: Iterable[T], k: int, rng: random.Random = None) -> List[T]:
    """
    Classic Algorithm R reservoir sampling.
    Selects k items uniformly at random from stream.
    """
    if k <= 0:
        return []
    r = rng if rng is not None else random
    reservoir: List[T] = []
    for i, item in enumerate(iterable):
        if i < k:
            reservoir.append(item)
        else:
            j = r.randint(0, i)
            if j < k:
                reservoir[j] = item
    return reservoir
