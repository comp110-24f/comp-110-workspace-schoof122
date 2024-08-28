"""Functions: Challenege Question #1"""

__author__ = "730674279"


def mimic(message: str) -> str:
    """Repeats your string back to you"""
    return message


def main() -> None:
    """Pulls functions together"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
