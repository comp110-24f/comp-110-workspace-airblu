"""Dictionary creation."""

__author__ = "730643371"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the dictionary."""
    inverted_dictionary: dict[str, str] = {}
    for key_1 in dictionary:  # sort thru the first side of ==
        for key_2 in dictionary:  # sort thru other side of ==
            if key_2 != key_1:  # insures keys are not the same
                if dictionary[key_1] == dictionary[key_2]:
                    raise KeyError("error message of your choice here!")

    for idx in dictionary:
        save_str: str = dictionary[idx]
        save_key: str = idx
        inverted_dictionary[save_str] = save_key  # code inverted to a new dict
    dictionary = {}
    for index in inverted_dictionary:  # makes new dict equal inputed dict
        dictionary[index] = inverted_dictionary[index]
    return dictionary


def favorite_color(color_choice: dict[str, str]) -> str:
    """Finds most common favorite color."""
    color_count: dict[str, int] = {}
    max_location: str = ""
    max: int = 0
    for idx in color_choice:
        if color_choice[idx] in color_count:  # checks if it already in the dict
            color_count[color_choice[idx]] = 1 + color_count[color_choice[idx]]
        if not color_choice[idx] in color_count:  # adds if it is not
            color_count[color_choice[idx]] = 1
    for key in color_count:
        if color_count[key] > max:
            max = color_count[key]
            max_location = key
    return max_location


def count(inpt: list[str]) -> dict[str, int]:
    """Creates a dictionary of amount of appearances."""
    counting: dict[str, int] = {}
    idx: int = 0
    while idx < len(inpt):  # change for while loop, similar to favorite_color
        if inpt[idx] in counting:
            counting[inpt[idx]] += 1
        if inpt[idx] not in counting:
            counting[inpt[idx]] = 1
        idx += 1
    return counting


def alphabetizer(list_1: list[str]) -> dict[str, list[str]]:
    """Alphabetizes a list of inputs."""
    alphabetized: dict[str, list[str]] = {}
    index: int = 0
    while index < len(list_1):
        if list_1[index][0].lower() in alphabetized:
            alphabetized[list_1[index][0].lower()] += [list_1[index]]
        if list_1[index][0].lower() not in alphabetized:
            alphabetized[list_1[index][0].lower()] = [list_1[index]]
        index += 1
    return alphabetized


def update_attendance(attendance: dict[str, list[str]], dow: str, name: str) -> None:
    """Updates list of attendance."""
    if dow in attendance:
        for key_1 in attendance:  # sort thru the first side of ==
            for key_2 in attendance:  # sort thru other side of ==
                if key_2 != key_1:  # insures keys are not the same
                    if not attendance[key_1] == attendance[key_2]:
                        attendance[dow] += [name]
    if dow not in attendance:
        attendance[dow] = [name]
    return None
