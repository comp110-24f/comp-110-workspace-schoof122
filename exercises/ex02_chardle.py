"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730674279"


def input_word() -> str:
    word: str = str(input("Enter a 5-character word:"))
    if len(word) == 5:
        print(word)
    else:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


input_word()
# exit function must go in the else block with the error message
# otherwise the entire function is canceled.


def input_letter() -> str:
    letter: str = str(input("Enter a single character:"))
    if len(letter) == 1:
        print(letter)
    else:
        print("Error: Character must be a single character.")
        exit()
    return letter


input_letter()
# used get_weather_report function example from class to format
# input_letter and input_word functions.


def contains_char(input_letter, input_word) -> None:
    print("Searching for " + str(input_letter) + " in " + str(input_word))
    if input_word[0] == input_letter:
        print(str(input_letter) + " found at Index 0")
    elif input_word[1] == input_letter:
        print(str(input_letter) + " found at Index 1")
    elif input_word[2] == input_letter:
        print(str(input_letter) + " found at Index 2")
    elif input_word[3] == input_letter:
        print(str(input_letter) + " found at Index 3")
    elif input_word[4] == input_letter:
        print(str(input_letter) + " found at Index 4")
    else:
        print("Error: Character must be a single character.")


print(contains_char(input_letter(), input_word()))
