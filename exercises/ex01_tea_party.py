"""Calculate cost of tea party given attendants."""

__author__: str = "730643371"


def main_planner(guests: int) -> None:
    """Defining main planner function."""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # this works but the rest do not
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # got this working now the rest dont
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # needed more parenthesis here
    return None


# Yipeeeeee it runs now


"""Defining the tea bag function."""


def tea_bags(people: int) -> int:
    """Return Function."""
    return people * 2


"""Defining the treat function."""


def treats(people: int) -> int:
    """return function."""
    return int(
        tea_bags(people=people) * 1.5
    )  # took some thought to realize I needed int()


"""Defining the cost function."""


def cost(tea_count: int, treat_count: int) -> float:
    """return function"""
    return float(
        (tea_count * 0.50) + (treat_count * 0.75)
    )  # getting error, fixed by changing return


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
