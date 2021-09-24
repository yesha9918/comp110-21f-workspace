"""List utility functions."""

__author__ = "730402890"


def all(x: list[int], y: int) -> bool:
    """Matching all items in list with integer provided."""
    i: int = 0
    if len(x) == 0:
        return False
    while i < len(x):
        if x[i] != y:
            return False
        i += 1
    return True


def is_equal(x: list[int], y: list[int]) -> bool:
    """Compares two lists to see if they're exactly the same."""
    i: int = 0
    if len(x) == len(y):
        while i < len(x):
            if x[i] != y[i]:
                return False
            i += 1
        return True
    else:
        return False


def max(x: list[int]) -> int:
    """Determines the max number in a list."""
    i: int = 0
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    max_number: int = x[0]
    while i < len(x):
        if max_number < x[i]:
            max_number = int(x[i])
        i += 1
    return max_number