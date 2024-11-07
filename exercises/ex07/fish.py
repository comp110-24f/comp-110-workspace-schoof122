"""File to define Fish class."""

__author__ = "730674279"


class Fish:
    """Class to define fish population."""

    age: int

    def __init__(self):
        """Defines fish class parameters (initialization)."""
        self.age = 0
        return None

    def one_day(self):
        """Reflects changes in the fish over one day."""
        self.age += 1
        return None


# Added the self.age attributes with no troubles
