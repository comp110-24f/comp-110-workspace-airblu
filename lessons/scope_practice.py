word: str = "yoyo"


def chars(msg: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = msg  # Set up empty str to copy values over
    idx: int = 0
    while idx <= len(msg):
        print(idx)
        idx += 1
    return copy


a: str = "Hey"
b: str = "Hi"
chars(msg=a)

"""if __name__ == "__main__":  # makes it so it only runs if you are in this specific file
    # python makes name variable automatically and calls it __main__
    print(remove_chars(word, "y"))"""
