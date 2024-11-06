"""File to define Fish class."""

__author__ = "730643371"


class Fish:
    """Define Fish class."""

    age: int

    def __init__(self):
        """Initializes fish."""
        self.age = 0
        return None

    def one_day(self):
        """One day added in fishland."""
        self.age += 1
        return None
