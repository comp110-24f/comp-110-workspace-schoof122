"""EX04 -- List Utility Functions"""

__author__ = "730674279"


def all(a: list[int], b: int) -> bool:
    """Compares a given int to a list of ints; checks to see if they're the same"""
    if a == []:
        return False
    idx: int = 0
    while idx < len(a):
        if a[idx] == b:
            idx += 1
        else:
            return False
    return True


# Had some difficulty with getting the loop to check all ints before
# providing a return statement.
# Used the idx variable in conjunction with "a" to tell the
# function to cycle through all options before returning True.
# Used else to break the loop early and return False
# in the case of a value on the list not matching the given int


def max(input: list[int]) -> int:
    """Returns the largest value in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 1
    big_number: int = input[0]
    while idx < len(input):
        if input[idx] > big_number:
            big_number = input[idx]
        idx += 1
    return big_number


# Most of the code was written before going to tutoring
# Had input[idx] set to equal big_number instead of the other way around
# Was returning idx instead of big_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Will determine if two lists are the same/equal to one another"""
    if len(list_1) != len(list_2):
        return False
    idx: int = 0
    while idx < len(list_1):
        if list_1[idx] == list_2[idx]:
            idx += 1
        else:
            return False
    return True


# Used the code from the all function
# Changed variables and set indicies equal to one another
# Added if statement above idx to make the function return false
# if presented with lists that were not equal


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Combines two lists into one longer list"""
    for item in list_2:
        list_1.append(item)


# First attempt at for...in loop! Created "item" and then
# appended it onto list_1
