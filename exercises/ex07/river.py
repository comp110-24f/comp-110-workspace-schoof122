"""File to define River class."""

__author__ = "730674279"
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Class to allow interaction of bears and fish."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of fish and bears to determine mortality."""
        surviving_fish: list = []
        surviving_bears: list = []
        for bear in self.bears:
            while bear.age <= 5:
                surviving_bears.append(bear)
        for fish in self.fish:
            while fish.age <= 3:
                surviving_fish.append(fish)
        self.bears = surviving_bears
        self.fish = surviving_fish
        return None

    # Created empty lists to reflect changes in the population
    # Set the original self lists equal to these at the end
    # While the ages of the bears or fish are less than 5 and 3, respectively
    # They are added to the list of survivors
    # Otherwise they aren't added, and so are removed from the population

    def bears_eating(self):
        """Updates hunger score and fish population based off how much bears eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None

    # Went to tutoring for help revising this function
    # Used .eat to modify the bear's hunger score and remove_fish to
    # reflect changes in the fish population

    def check_hunger(self):
        """Checks to see if bears have eaten enough or if they starve."""
        surviving_bears: list = []
        for bear in self.bears:
            if bear.hunger_score > 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    # Created empty list so that I could set self.bears equal to it at
    # the end of the funtion to reflect changes in the bear population
    # Used a for in loop to iterate through each bear in the list
    # Used an if statement to determine if the bear survived.

    def repopulate_fish(self):
        """Controls repopulation of fish."""
        for fish in self.fish:
            if len(self.fish) // 2 * 4 > 0:
                self.fish.append(fish)
        return None

    def repopulate_bears(self):
        """Controls repopulation of bears."""
        for bears in self.bears:
            while len(self.bears) // 2 > 0:
                self.bears.append(bears)
        return None

    def view_river(self):
        """Allows you to view the status of the river (day, #fish, #bears)."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

        return None

    # Used f strings to create the print statements for view_river
    # Was originally printing the entire self.fish list; had to change to len
    # to get the number of fish remaining

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

    def one_river_week(self):
        """Simulates one week of life in the river."""
        x: int = 0
        while x < 7:
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Removes fish eaten by bears."""
        remaining_fish: list = []
        for i in range(amount, len(self.fish)):
            remaining_fish.append(self.fish[i])
        self.fish = remaining_fish


# Went to tutoring for help revising the remove_fish function
# Implemented the for in loop and used range to determine which fish would be removed
# set the new list equal to self.fish to update it to reflect the missing fish
