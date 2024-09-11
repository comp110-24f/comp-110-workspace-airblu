def greet(name: str) -> None:
    print("I'm so happy to see you " + name + "!")
    print(
        "Hello "
        + name
        + ", your name starts with an "
        + str(name[0])
        + " and ends with an "
        + str(name[len(name) - 1])
    )


def main() -> None:
    print(greet(name="Molly"))


# Example usage:
main()
