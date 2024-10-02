"""recreating wordle"""

__author__ = "730643371"


def input_guess(secret_word_len: int) -> str:
    """gets imput with correct number of letters"""
    guess: str = str(
        input("Enter a " + str(secret_word_len) + " character word: ")
    )  # had to edit to accomidate longer words
    while len(guess) != secret_word_len:
        guess = input("That wasn't " + str(secret_word_len) + " chars! Try again: ")
    return guess


def contains_char(word: str, letter: str) -> bool:
    """sorting through the word for letter"""
    assert len(letter) == 1
    idx: int = 0
    bool_val: bool = False
    while idx < len(word):
        if word[idx] == letter:
            bool_val = True  # avoid infitine loop
            idx = len(word)
        else:
            idx += 1
    return bool_val


def emojified(guess: str, secret_word: str) -> str:
    """Compare two strings of equal length"""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    output: str = ""
    yellow_indicator: bool = False
    while index < len(guess):
        if guess[index] == secret_word[index]:
            output = f"{output}{GREEN_BOX}"
        else:
            yellow_indicator = contains_char(secret_word, guess[index])
            if yellow_indicator:
                output = f"{output}{YELLOW_BOX}"
            else:
                output = f"{output}{WHITE_BOX}"  # use proper formatting
        index += 1

    return output


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 0
    win: bool = False
    letter_count: int = len(secret)  # adj for varying len
    while turn < 6 and (not (win)):
        print("=== Turn " + str(turn + 1) + "/6" + " ===")
        user_input: str = input_guess(
            letter_count
        )  # assign to variable so only prompted once
        print(emojified(user_input, secret))
        if secret == user_input:
            win = True
            print("You won in " + str(turn + 1) + "/6 turns!")
        else:
            turn += 1
    if not win:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
