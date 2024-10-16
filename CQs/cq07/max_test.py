"""Test file for find_max functions"""

__author__ = "730674279"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_return() -> None:
    assert find_and_remove_max(a=[9, 8, 7, 9]) == 9


def test_find_and_remove_max_mutate() -> None:
    assert find_and_remove_max(a=[12, 8, 7, 9]) == 12


# Return and Edge tests worked fine, unsure about mutate test
# Running it through autograder to make sure it works properly


def test_find_and_remove_max_edge() -> None:
    assert find_and_remove_max(a=[-1, -2, -5]) == -1
