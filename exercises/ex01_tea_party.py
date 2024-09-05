"""A file to plan a cozy tea party!"""

__author__ = "730674279"


def main_planner(guests: int) -> None:
    """Calculates costs, amount of teas, and amount of treats"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """The number of tea bags needed for the party"""
    return people * 2


# Had trouble figuring out the return type; was able to use error message
# and directions to remember to return people * 2 instead of int.
# Return line is NOT the same as return type!


def treats(people: int) -> int:
    """The amount of treats needed for the party"""
    return int(1.5 * tea_bags(people=people))


# I spent two hours on this and I honestly don't know how I figured it out
# Spent a while assuming that the return type would just be "tea_bags" without
# anything in parentheses after.
# Eventually realized this was wrong by going back through
# the presentations and looking at examples.
# Knew that 1.5 needed to be converted to
# an int (used the int() built-in function)
# Kept getting return values of 8 and 4
# when testing; I had an extra multiplier I didn't need.


def cost(tea_count: int, treat_count: int) -> float:
    """Determines the cost of the party"""
    return (0.50 * (tea_count)) + (0.75 * (treat_count))


# Went to tutoring for help with cost and main_planner functions
# Discussed syntax errors and how calling a function
# is NOT the same as multiplying or adding one
# Adding strings = put everything after print in parentheses
# Write the string and then convert the rest to a string as well.


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
