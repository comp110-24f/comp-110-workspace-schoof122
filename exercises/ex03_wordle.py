"""EX03 - Wordle - A fun word-guessing game!"""

__author__ = "730674279"


def input_guess(secret_word_len: int) -> str:
    """Allows the user to guess a word of the correct length"""
    word: str = str(input(f"Enter a {secret_word_len} character word: "))
    while secret_word_len != len(word):
        word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return word


# Struggled with the first attempt at a while loop
# Managed to put most of the code together independently; went to tutoring to work
# out some bugs(while loop was running infinitely
# or not allowing the user to try again)
# Needed to set input equal to word within the loop to fix this problem


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Finds instances of a character within the given word"""
    assert len(char_guess) == 1
    idx: int = 0
    while len(secret_word) > idx:
        if secret_word[idx] == char_guess:
            return True
        idx += 1
    return False


# Was able to define function and set up parameters, used the assert statement
# Created an index, used this and Boolean values to run the loop
# Had to learn through experimentation with len(secret_word) > idx
# (Originally had it as >= or =)


def emojified(user_guess: str, secret_word: str) -> str:
    """Adds colored emojis to signify correctness of guess"""
    assert len(user_guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    boxes: str = ""
    idx: int = 0
    while len(secret_word) > idx:
        if secret_word[idx] == user_guess[idx]:
            boxes += GREEN_BOX
        elif contains_char(secret_word=secret_word, char_guess=user_guess[idx]):
            boxes += YELLOW_BOX
        else:
            boxes += WHITE_BOX
        idx += 1
    return boxes


# Imported the emoji hex codes, used these to make the "boxes" variable work
# Got help with the loop at tutoring again
# It was difficult to correctly implement contains_char
# I was forgetting to provide arguments to the parameters in that function.


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    guess: int = 1
    word_guess: str = ""
    while guess <= 6:
        print(f"=== Turn {guess}/6 ===")
        word_guess = input_guess(secret_word_len=5)
        print(emojified(user_guess=word_guess, secret_word=secret))
        if word_guess == secret:
            print(f"You won in {guess}/6 turns!")
            guess = 7
        elif guess == 6:
            print("X/6 - Sorry, try again tomorrow!")
        guess += 1


# Didn't incorporate word_guess until much later
# (this caused trouble with the while loop)
# The emojified function was running but not providing the emojis
# Fixed this at tutoring by adding in the arguments word_guess and secret
# Also turned the function call into a print statement.

if __name__ == "__main__":
    main(secret="codes")
