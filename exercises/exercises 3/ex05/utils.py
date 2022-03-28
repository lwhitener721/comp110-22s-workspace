"""Collection of functions that I am going to test."""

__author__ = "739479707"


def only_evens(xs: list[float]) -> list:
    """Return only evens in this list.""" 
    evens: list = []
    for num in xs:
        if num % 2 == 0:
            evens.append(num)
    return evens 

    
def sub(xs: list[int], start: int, end: int) -> list:
    """Generating a subset of a list."""
    a_list: list = []
    while start < end:
        if start < 0:
            start = 0
        if end > len(xs):
            end = len(xs)
        a_list.append(xs[start])
        start += 1
    return a_list 


def concat(x: list[int], y: list[int]) -> list:
    """Returns both lists in a single list."""
    z = x + y 
    return z
