"""Exercise w/ Lists!"""

__author__ = "730643371"


def all(list: list[int], number: int) -> bool:
    """Finds if all numbers in list match the number."""
    idx: int = 0
    same: bool = False
    same_count: int = 0  # create counter to compare total matches to len of list
    while idx < len(list):  # change bool operator from > to <
        if list[idx] == number:
            same_count += 1
        idx += 1
    if same_count == len(list):
        same = True
    if len(list) == 0:
        same = False
    print(same)
    return same


def max(input: list[int]) -> int:
    """Find max number."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
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
    print(max_number)
    return max_number


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Find if lists are equal."""
    ix: int = 0
    same_count: int = 0
    same: bool = False
    while ix < len(list1) and ix < len(list2):
        if list1[ix] == list2[ix]:
            same_count += 1
        ix += 1
    if same_count == len(list1) and same_count == len(list2):
        same = True
    print(same)
    return same


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Recreating extend."""
    indx: int = 0
    while indx < len(list_2):
        list_1.append(list_2[indx])
        indx += 1
