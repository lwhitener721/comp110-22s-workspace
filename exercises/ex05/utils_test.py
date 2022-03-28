"""Not sure what this is for."""

__author__ = "730479707"

from utils import only_evens, concat, sub 


def test_only_evens() -> None:
    """Testing if only_evens returns empty list."""
    xs: list[float] = [] 
    assert only_evens(xs) == []


def test_only_evens_evens() -> None:
    """Testing if only_evens returns evens in a list."""
    xs: list[float] = [1.0, 2.0, 3.0, 4.0] 
    assert only_evens(xs) == [2.0, 4.0]


def test_only_evens_neg_evens() -> None:
    """Testing if only_evens returns negative evens in a list."""
    xs: list[float] = [1.0, -2.0, 2.0, -4.0, 3.0, 4.0] 
    assert only_evens(xs) == [-2.0, 2.0, -4.0, 4.0]


def test_only_evens_one() -> None:
    """Testing if only_evens returns singular evens in a list."""
    xs: list[float] = [2.0] 
    assert only_evens(xs) == [2.0]


def test_sub_negative() -> None:
    """Testing if sub."""
    assert sub([1, 2, 3], 1, 2) == [2]


def test_sub() -> None:
    """Testing if sub."""
    assert sub([1, 2, 3, 4, 5], 0, 3) == [1, 2, 3]


def test_sub_again() -> None:
    """Testing if sub."""
    assert sub([1, 2, 3], 2, 3) == [3]


def test_concat() -> None:
    """Testing to see if concat returns an empty list when given two empty lists."""
    x: list[int] = [] 
    y: list[int] = [] 
    assert concat(x, y) == []


def test_concat_multiple() -> None:
    """Testing to see if concat returns the added lists together."""
    x: list[int] = [1, 2, 3] 
    y: list[int] = [4, 5, 6] 
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]


def test_concat_single() -> None:
    """Testing to see if concat returns list when given two lists."""
    x: list[int] = [2] 
    y: list[int] = [3] 
    assert concat(x, y) == [2, 3]