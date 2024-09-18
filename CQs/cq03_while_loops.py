"""Functions: Challenge Question 3"""

__author__ = "730674279"


def num_instances(phrase: str, search_char: str) -> int:
    index: int = 0
    count: int = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count = count + 1
        index = index + 1
    return count
