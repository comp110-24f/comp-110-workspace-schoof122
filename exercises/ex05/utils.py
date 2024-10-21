"""List utility functions"""

__author__ = "730674279"


def only_evens(a: list[int]) -> list[int]:
    """Returns only the even elements of a list"""
    idx: int = 0
    new_list: list = []
    while idx < len(a):
        if a[idx] % 2 == 0:
            new_list.append(a[idx])
        idx += 1
    return new_list


# Started by making idx, new_list, and while loop
# It took an embarrassingly long time to remember modulo existed
# After that, wrote if statement and tested in the terminal


def sub(z: list[int], number_1: int, number_2: int) -> list[int]:
    """Returns a part of the given list between the start index and end index minus 1"""
    new_list: list = []
    idx: int = number_1
    if number_1 < 0:
        number_1 = z[0]
    if number_2 > len(z):
        number_2 = len(z)
    if len(z) == 0:
        return []
    if number_1 >= len(z):
        return []
    if number_2 <= 0:
        return []
    while idx < number_2:
        new_list.append(z[idx])
        idx += 1
    return new_list


# Put together all if statements without trouble
# Except for if number_1 is less than 0
# It keeps resulting in an empty list
# While statement was effective after first test


def add_at_index(list: list[int], added_element: int, index_number: int) -> None:
    """Modifies the input list to place an element at a given index"""
    if index_number < 0:
        raise IndexError("Index is out of bounds for the input list")
    elif index_number > len(list):
        raise IndexError("Index is out of bounds for the input list")
    else:
        list.append(0)
    idx: int = 0
    while idx < len(list) - (index_number + 1):
        list[len(list) - (idx + 1)] = list[len(list) - (idx + 2)]
        idx += 1
    list[index_number] = added_element


# Went to office hours for help with add_at_index function
# Originally was using the "insert" construct
# Remodeled to use a while loop to iterate through the list,
# Added an empty space and then moved each element to the right
# until the empty space was even with the desired index_number
# Then made that spot on the list equal to the added_element
# (Basically append w/o using append)
