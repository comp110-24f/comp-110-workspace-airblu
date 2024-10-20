"""Defining find max function."""

__author__: str = "730643371"


def find_and_remove_max(input: list[int]) -> int:
    """Find max number."""
    if len(input) == 0:
        return -1
    index: int = 0
    max_number: int = 0
    while index < len(input):
        if input[index] < max_number:
            max_number = input[index]
        index += 1
    idx: int = 0
    while idx < len(input):
        if input[idx] > max_number:
            max_number = input[idx]
        idx += 1
    idx: int = 0
    while idx < len(input):
        if input[idx] == max_number:
            input.pop(idx)
            idx -= 1
        idx += 1
    print(input)
    return max_number
