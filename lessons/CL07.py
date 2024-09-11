"""Practicing my conditionals"""


def less_than_ten(num: int) -> None:
    """tell us if num is less than ten"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small lil number:(")
    else:
        print("huge number")
    print("Toodles")


less_than_ten(num=11)


def wake_up(alarm: bool) -> str:
    if alarm is True:
        return "wake up!"
    else:
        return "back to sleep"


# print(wake_up(alarm=False))- disabled


def check_first_letter(word: str, letter: str) -> None:
    if word[0] == letter:
        print("match!")
    else:
        print("no match :(")


# check_first_letter(word="happy", letter="h")
