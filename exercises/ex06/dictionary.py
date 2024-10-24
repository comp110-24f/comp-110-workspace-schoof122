"""Practice with Dictionary Utility Functions"""

__author__ = "730674279"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Will swap the keys and values of the function"""
    for item in dictionary:
        count: int = 0
        for value in dictionary:
            if dictionary[value] == dictionary[item]:
                count += 1
        if count >= 2:
            raise KeyError("Cannot have duplicate keys")
    inverted_dictionary = {}
    for item in dictionary:
        inverted_dictionary[dictionary[item]] = item
    return inverted_dictionary


# Went to tutoring for help with establishing swapping of keys and values
# Was able to swap one or the other, but not both
# Used count and nested loops to check for duplicate keys
# Created an empty dictionary to store values
# Line 17 swaps the keys and values


def favorite_color(colors: dict[str, str]) -> str:
    """Takes names and favorite colors; returns the most popular color"""
    new_dictionary: dict[str, int] = {}
    for keys in colors:
        if colors[keys] in new_dictionary:
            new_dictionary[colors[keys]] += 1
        else:
            new_dictionary[colors[keys]] = 1
    highest_count: int = 0
    color: str = ""
    for keys in new_dictionary:
        if new_dictionary[keys] > highest_count:
            highest_count = new_dictionary[keys]
            color = keys
    return color


# Created an empty dictionary to organize the colors and their frequency
# Used a for loop and if/else statements to check how often a color appeared
# Highest_count variable established to pick the most popular color
# Created another loop to cycle through the new dictionary and find the most
# popular color.


def count(a: list[str]) -> dict[str, int]:
    """Takes a list and returns a dicitonary with list items as
    keys and frequency as values"""
    results: dict[str, int] = {}
    for item in a:
        if item in results:
            results[item] += 1
        else:
            results[item] = 1
    return results


# Used a similar counting method to above to check how often a key appeared
# in a given list
# Created an empty dictionary to store the new keys and values


def alphabetizer(m: list[str]) -> dict[str, list[str]]:
    """Produces a dictionary with letters as keys and words beginning
    with that letter as values"""
    alphabet: dict[str, list[str]] = {}
    for item in m:
        item = item.lower()
        if item[0] in alphabet:
            alphabet[item[0]].append(item)
        else:
            alphabet[item[0]] = [item]
    return alphabet


# Created empty dictionary and for loop to cycle through list
# Added lower function to undo case sensitivity
# If statement = if the first letter of the word (c of item cat) is in the dictionary
# Add that item in at the letter (key)
# Otherwise, add in the letter (key) and the item


def update_attendance(
    days_students: dict[str, list[str]], weekday: str, student: str
) -> None:
    """Provides a record of attendance for students based on days of the week"""
    if weekday in days_students:
        if student not in days_students[weekday]:
            days_students[weekday].append(student)
    else:
        days_students[weekday] = [student]


# If the weekday already exists in the dictionary
# Do this if statement: where if the student is not there, append them
# At that weekday (key)
# Otherwise, add the weekday (key) and the student (value)
