from lessons.unit_tests.list_fns import get_and_remove_first, get_first, remove_first


def test_get_first() -> None:
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert get_first(fruits) == "apples"


def test_remove_first_return_value() -> None:
    """Test remove first returns none."""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert remove_first(fruits) == None


def test_remove_first_behavior() -> None:
    """Test remove first removes first element."""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    remove_first(fruits)
    assert fruits == ["oranges", "bananas"]


"""def test_get_first_edge_case() -> None:
    Test for empty list.
    list: list[str] = []
    assert get_first([]) == """ ""
