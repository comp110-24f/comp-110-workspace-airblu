"""Writing Functions CQs"""

__author__: str = "730643371"

"""defining mimic"""


def mimic(message: str) -> str:
    return str(message)


def main() -> None:
    print(mimic(message=input("What is your message?")))
    return None


if __name__ == "__main__":
    main()
