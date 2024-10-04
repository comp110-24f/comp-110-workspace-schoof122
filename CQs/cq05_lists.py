"""Mutating Functions"""

__author__ = "730674279"


def manual_append(a: list[int], b: int) -> None:
    """Appends an int onto a list"""
    a.append(b)


# Added in the parameters list[int] and [int]
# by naming them as "a" and "b"
# Used the append modifier to add "b" to the end of "a"


def double(c: list[int]) -> None:
    """Multiplies all list elements by 2"""
    idx: int = 0
    while idx < len(c):
        c[idx] *= 2
        idx += 1


# While loop used to sort through all indexes of "c"
# Everything was initially correct except syntax for multiplication
# And unecessary print statement
# Corrected these issues and ran tests

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
