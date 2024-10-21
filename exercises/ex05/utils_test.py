"""Tests for list utility functions"""

__author__ = "730674279"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index
import pytest


def test_only_evens() -> None:
    """Will assess the only_evens function to see if it returns the correct values"""
    assert only_evens(a=[3, 6, 9, 12]) == [6, 12]


def test_only_evens_2() -> None:
    """Will assess the only_evens function to make sure it does not mutate the input"""
    assert only_evens(a=[2, 2, 2, 4, 6]) == [2, 2, 2, 4, 6]


def test_only_evens_3() -> None:
    """An edge case test for the only_evens function"""
    assert only_evens(a=[]) == []


def test_sub() -> None:
    """Will assess the sub function to see if it returns the correct list section"""
    assert sub(z=[6, 7, 8, 9, 10, 12], number_1=2, number_2=5) == [8, 9, 10]


def test_sub_2() -> None:
    """Tests that the sub function does not mutate the input list"""
    assert sub(z=[120, 121, 122, 138], number_1=1, number_2=3) == [121, 122]


def test_sub_3() -> None:
    """Edge case test for empty list"""
    assert sub(z=[], number_1=7, number_2=9) == []


def test_add_at_index() -> None:
    """Test add_at_index to see if it functions as expected"""
    assert add_at_index(list=[3, 4, 5, 6, 8], added_element=7, index_number=4) is None


# Didn't set assert = None originally, so I kept getting an assertion error
# Fixed in office hours


def test_add_at_index_2() -> None:
    """Edge case test for add_at_index function"""
    with pytest.raises(IndexError):
        add_at_index(list=[1, 2, 3], index_number=5, added_element=4)


# Used syntax provided in instructions to check if the Index Error would
# be raised properly


def test_add_at_index_3() -> None:
    """Test add_at_index to see if it correctly modifies the list"""
    c: list[int] = [5, 6, 7, 8, 10]
    add_at_index(c, added_element=9, index_number=4)
    assert c == [5, 6, 7, 8, 9, 10]


# Set a list as a variable, then called it using the add_at_index function
# asserted the variable set equal to the correct output list to check functionality
