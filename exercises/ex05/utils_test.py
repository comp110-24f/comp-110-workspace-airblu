"""Testing utils."""

__author__ = "730643371"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_return_val() -> None:
    test_case_1: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(test_case_1) == [2, 4]


def test_only_evens_list_mod() -> None:
    test_case_2: list[int] = [1, 2, 3, 4, 5]
    only_evens(test_case_2)
    assert test_case_2 == [1, 2, 3, 4, 5]


def test_only_evens_edge_case() -> None:
    test_case_3: list[int] = [1, 3, 5]
    assert only_evens(test_case_3) == []


def test_sub_return_val() -> None:
    test_case_4: list[int] = [10, 20, 30, 40]
    assert sub(test_case_4, 1, 3) == [20, 30]


def test_sub_list_mod() -> None:
    test_case_5: list[int] = [1, 2, 3, 4, 5]
    sub(test_case_5, 1, 4)
    assert test_case_5 == [1, 2, 3, 4, 5]


def test_sub_edge_case() -> None:
    test_case_6: list[int] = []
    assert sub(test_case_6, 1, 3) == []


def test_add_at_index_return_val() -> None:
    test_case_7: list[int] = [1, 2, 3, 5]
    assert add_at_index(test_case_7, 4, 3) is None


def test_add_at_index_mod() -> None:
    test_case_8: list[int] = [1, 2, 3, 5]
    add_at_index(test_case_8, 4, 3)
    assert test_case_8 == [1, 2, 3, 4, 5]


def test_add_at_index_edge_case() -> None:
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    with pytest.raises(IndexError):
        add_at_index([], 1, 1)
        # an IndexError is raised for the case when the add_at_index is given an input
        # that is greater than the length of our <list_object>
