"""EX04 -- List Utility Functions"""

__author__ = "730674279"


def all(a: list[int], b: int) -> bool:
    """Compares a given int to a list of ints; checks to see if they're the same"""
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
    idx: int = 0
    while idx < len(input):
        if input[idx] > idx + 1:
            print(input[idx])
        idx += 1
    return idx


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Will determine if two lists are the same/equal to one another"""
    idx: int = 0
    while idx < len(list_1 or list_2):
        if list_1[idx] == list_2[idx]:
            idx += 1
        else:
            return False
    return True


# Used the code from the all function
# Changed variables and set indicies equal to one another in line 41


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Combines two lists into one longer list"""
