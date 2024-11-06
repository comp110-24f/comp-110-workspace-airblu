"""File to define River class."""

__author__ = "730643371"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Defines river class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New river with num_fish Fish and num_bears bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def one_river_week(self) -> None:
        """Runs one river week 7 times."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None

    def check_ages(self):
        """Ensures ages are correct."""
        new_fish_list: list[Fish] = []
        for key in self.fish:
            if key.age <= 3:
                new_fish_list.append(key)
        self.fish = new_fish_list

        new_bear_list: list[Bear] = []
        for key in self.bears:
            if key.age <= 5:
                new_bear_list.append(key)
        self.bears = new_bear_list

    def bears_eating(self):
        """Simulates bears eating."""
        while len(self.fish) > 5:
            self.remove_fish(3)
            for idx in self.bears:
                Bear.eat(idx, num_fish=3)
        return None

    def check_hunger(self):
        """Checks bear hunger."""
        alive_bears: list[Bear] = []
        for idx in self.bears:  # use idx as your self
            if idx.hunger_score >= 0:
                alive_bears.append(idx)
        self.bears = alive_bears
        return None

    def repopulate_fish(self):
        """Adds more fish."""
        new_fish: int = 4 * (len(self.fish) // 2)  # mult by 4
        idx: int = 0
        while idx < new_fish:
            self.fish.append(Fish())
            idx += 1
        return None

    def repopulate_bears(self):
        """Adds more bears."""
        new_bears: int = len(self.bears) // 2
        idx: int = 0
        while idx < new_bears:
            self.bears.append(Bear())
            idx += 1
        return None

    def view_river(self):
        """Prints out river data."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def remove_fish(self, amount: int) -> None:
        """Gets rid of a certain nuber of fish."""
        for idx in range(0, (amount)):
            self.fish.pop(idx)
