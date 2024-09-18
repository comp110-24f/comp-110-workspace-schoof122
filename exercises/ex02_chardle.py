"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730674279"


def input_word() -> str:
    """Allows the user to imput a word"""
    word: str = str(input("Enter a 5-character word: "))
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


# exit function must go in the else block with the error message
# otherwise the entire function is canceled.
# return statement must go in 'if' block; otherwise you return word + error message


def input_letter() -> str:
    """Allows the user to imput a letter"""
    letter: str = str(input("Enter a single character: "))
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


# used get_weather_report function example from class to format
# input_letter and input_word functions.


def contains_char(input_word: str, input_letter: str) -> None:
    """Searches for instances of a character within a given word"""
    print("Searching for " + str(input_letter) + " in " + str(input_word))
    count: int = 0
    if input_word[0] == input_letter:
        print(str(input_letter) + " found at index 0")
        count += 1
    if input_word[1] == input_letter:
        print(str(input_letter) + " found at index 1")
        count += 1
    if input_word[2] == input_letter:
        print(str(input_letter) + " found at index 2")
        count += 1
    if input_word[3] == input_letter:
        print(str(input_letter) + " found at index 3")
        count += 1
    if input_word[4] == input_letter:
        print(str(input_letter) + " found at index 4")
        count += 1
    if count == 0:
        print(f"No instances of {input_letter} found in {input_word}")
    if count == 1:
        print(f"{count} instance of {input_letter} found in {input_word}")
    if count > 1:
        print(f"{count} instances of {input_letter} found in {input_word}")


# Typed out all lines of code for each index
# Replaced original 'else' statements with 'if' statements.
# Program was ending upon hitting the 'else' statement, so this fixed that.
# Added count variable to count the number of instances
# It must be included in all statements so that it can add up throughout the code
# Added 'if' statements to determine what prints depending on the final value of count
# Removed final print statement (called function in main).


def main() -> None:
    """Starts Chardle program"""
    contains_char(input_word(), input_letter())


if __name__ == "__main__":
    main()
