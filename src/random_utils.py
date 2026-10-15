"""Random selection, weighted sampling, and random code generation utilities."""

import random
import string
from typing import Any, Dict, List, Sequence, TypeVar

T = TypeVar("T")


def random_alphanumeric(length: int = 16) -> str:
    """Generate a random alphanumeric string."""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def weighted_choice(choices: Dict[T, float]) -> T:
    """Select an item randomly according to relative probability weights."""
    if not choices:
        raise ValueError("Choices cannot be empty.")
    items = list(choices.keys())
    weights = list(choices.values())
    return random.choices(items, weights=weights, k=1)[0]


def shuffle_copy(seq: Sequence[T]) -> List[T]:
    """Return a new list containing elements in shuffled order."""
    res = list(seq)
    random.shuffle(res)
    return res


def roll_dice(sides: int = 6, count: int = 1) -> List[int]:
    """Simulate rolling multiple dice with specified number of sides."""
    if sides < 1 or count < 1:
        raise ValueError("Sides and count must be at least 1.")
    return [random.randint(1, sides) for _ in range(count)]
