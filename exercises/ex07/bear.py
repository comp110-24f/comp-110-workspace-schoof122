"""File to define Bear class."""

__author__ = "730674279"


class Bear:
    """Class to define Bear population."""

    age: int
    hunger_score: int

    def __init__(self):
        """Defines bear class parameters (initialization)."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Reflects changes in the bears over one day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Reflects the hunger score of bears in reference to fish eaten."""
        self.hunger_score += num_fish


# This file was easy to modify using self.(attribute)
# It's a good breakdown of the bear class that was useful
# to refer back to while working on the assignment
