"""Mutating functions."""

__author__: str = "730643371"


def manual_append(list1: list[int], mutation: int) -> None:
    list1.append(mutation)


manual_append([1, 2, 3], 4)


def double(list2: list[int]) -> None:
    idx: int = 0
    while idx < len(list2):
        list2[idx] = 2 * list2[idx]
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
