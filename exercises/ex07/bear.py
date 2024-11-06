"""File to define Bear class."""

__author__ = "730643371"


class Bear:
    """define Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes bear."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """One day added in fishland."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Bears gotta eat."""
        self.hunger_score += num_fish
        return None
