"""Example functions to practice testing"""

__author__ = "730674279"


def find_and_remove_max(a: list[int]) -> int:
    """Finds and removes the largest value"""
    if a == []:
        return -1
    idx: int = 0
    idx2: int = 0
    big_number: int = a[0]
    while idx < len(a):
        if a[idx] > big_number:
            big_number = a[idx]
        idx += 1
    while idx2 < len(a):
        if a[idx2] == big_number:
            a.pop(idx2)
        else:
            idx2 += 1
    return big_number


# Made while loop for big_number without trouble
# Added second while loop to pop the number
# Was popping big_number instead of idx2
# Corrected and added else statement
