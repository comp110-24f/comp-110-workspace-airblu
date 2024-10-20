"""Testing find_max function."""

__author__: str = "730643371"

from CQs.cq07.find_max import find_and_remove_max


def test_ind_and_remove_max_return() -> None:
    assert find_and_remove_max([10, 9, 8, 7, 10]) == 10


def test_ind_and_remove_max_mutate() -> None:
    b: list[int] = [10, 9, 8, 7, 10]
    find_and_remove_max(b)
    assert b == [9, 8, 7]


def test_ind_and_remove_max_edge_case() -> None:
    assert find_and_remove_max([]) == -1
