"""Summing the elements of a list using different loops"""

__author__ = "730674279"


def w_sum(vals: list[float]) -> float:
    """Takes a list and provides the sum of all inputs using a while loop"""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum = sum + vals[idx]
        idx += 1
    return sum


# Had while loop complete except for sum variable
# Added this and set equal to sum + vals[idx] so that
# the loop would add a new item from the list to sum each time


def f_sum(vals: list[float]) -> float:
    """Takes a list and provides the sum of all inputs using a for in loop"""
    sum: float = 0.0
    for elem in vals:
        sum = elem + sum
    return sum


# for_in loop also needed a sum variable
# Same method as before, minus the idx variable


def f_range_sum(vals: list[float]) -> float:
    """Takes a list and provides the sum of all inputs using a ranged for in loop"""
    sum: float = 0.0
    for elem in range(0, len(vals)):
        sum = elem + sum
    return sum


# Copy of above f_sum function with added range
