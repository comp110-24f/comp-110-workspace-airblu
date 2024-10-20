"""Defining 3 functions."""

__author__ = "730643371"


def only_evens(input: list[int]) -> list[int]:
    """Collects only evens."""
    evens: list[int] = []
    idx: int = 0
    while idx < len(input):
        if input[idx] % 2 == 0:
            evens.append(input[idx])
        idx += 1
    return evens


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Only highlights the selected range of values."""
    subbed: list[int] = []
    index: int = 0
    while index < len(input):
        while start <= index and index < end:
            if index < len(input):
                subbed.append(input[index])
            index += 1
            print(subbed)
        if start > index:
            index += 1
        if index >= end:
            index += len(input)
    return subbed


def add_at_index(inpt: list[int], num: int, idex: int) -> None:
    """Adds the number at the inputted index."""
    indx: int = 0
    output: list[int] = []
    if idex > (len(inpt)) or idex < 0:
        raise IndexError(
            "Index is out of bounds for the input list"
        )  # raise an error if the index is out of bounds
    while indx < len(inpt):
        if indx == idex:
            output.append(num)
        output.append(inpt[indx])
        indx += 1
    if idex == len(inpt):
        output.append(num)

    for i in range(0, len(output)):
        if i < len(inpt):
            inpt[i] = output[i]  # Replace the existing elements
        else:
            inpt.append(
                output[i]
            )  # Append the new elements if the original list is shorter
    while len(inpt) > len(
        output
    ):  # If the input list is longer than the output, remove the extra elements
        inpt.pop()  # Remove any extra elements from the original list
    return None
