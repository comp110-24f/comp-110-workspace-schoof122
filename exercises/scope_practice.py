def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
        index += 1
    return copy


word: str = "yoyo"
print(remove_chars(word, "y"))


def chars(msg: str) -> str:
    idx: int = 0
    copy: str = msg
    while idx < len(msg):
        print(msg[idx])
        idx += 1
    return copy


a: str = "hey"
b: str = "hi"
chars(msg=a)
