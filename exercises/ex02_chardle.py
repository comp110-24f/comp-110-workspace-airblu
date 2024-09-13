"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730643371"


def input_word() -> str:
    """Prompting for an Input Word"""
    final_word: str = input("enter a 5-character word: ")
    if len(final_word) == 5:
        return final_word
    else:
        print("Error: Word must contain 5 characters.")
        """exiting early"""
        exit()
        return final_word


def input_letter() -> str:
    """Prompting for an Input Letter"""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:  # needed to change parameter to word
    """Checking Indices for Matches"""
    print(
        "Searching for " + letter + " in " + word
    )  # put up top to print first before running rest
    count: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")  # use if, not elif or else
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)  # letter than word
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
