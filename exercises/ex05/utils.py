"""List utility functions part 2."""

__author__ = "730402890"


def only_evens(x: list[int]) -> list[int]:
    """Returning a list of ints with only even number inputs."""
    i: int = 0
    evens: list[int] = list()
    while i < len(x):
        if x[i] % 2 == 0:
            evens.append(x[i])
        i += 1
    return evens


def sub(x: list[int], start: int, end: int) -> list[int]:
    """Returning a list which is a subset of the given list, between the start and end index."""
    subs: list[int] = list()
    if start < 0:
        start = 0
        print(start)
    if end > len(x):
        end = len(x)
        print(end)
    if len(x) == 0 or start > len(x) or end <= 0:
        return subs
    while start < end:
        subs.append(x[start])
        start += 1
    return subs


def concat(x: list[int], y: list[int]) -> list[int]:
    """Concatting two lists into one list."""
    both: list[int] = list()
    i: int = 0
    while i < len(x):
        both.append(x[i])
        i += 1
    i = 0
    while i < len(y):
        both.append(y[i])
        i += 1
    return both