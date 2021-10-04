"""Unit tests for list utility functions."""


from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730402890"


def test_evens_only_empty() -> None:
    assert only_evens([]) == []


def test_evens_only_evens() -> None:
    assert only_evens([4, 3, 4]) == [4, 4]


def test_evens_only_odds() -> None:
    assert only_evens([1, 5, 3]) == []
 

def test_sub_empty() -> None:
    assert sub([], 3, 5) == []


def test_sub_negative() -> None:
    assert sub([1, 2], 3, -4) == []


def test_sub() -> None:
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_long() -> None:
    assert sub([1, 2, 3, 4], -4, 5) == [1, 2, 3, 4]


def test_concat() -> None:
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_empty() -> None:
    assert concat([], []) == []


def test_concat_one_empty() -> None:
    assert concat([], [1, 2]) == [1, 2]


def test_concat_single() -> None:
    assert concat([6], [9]) == [6, 9]