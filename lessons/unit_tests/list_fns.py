def get_first(list: list[str]) -> str:
    return list[0]


def remove_first(list: list[str]) -> None:
    list.pop(0)


def get_and_remove_first(list: list[str]) -> str:
    string: str = list[0]
    list.pop(0)
    return string
