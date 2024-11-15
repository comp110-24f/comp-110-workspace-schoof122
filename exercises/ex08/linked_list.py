"""Recursive functions exercise 8."""

from __future__ import annotations

# Imported module that allows Node to be used

__author__ = "730674279"


class Node:
    """Defines the Node class."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Initializes each Node."""
        self.value = val
        self.next = next

    # Initializes each object in the node class

    def __str__(self) -> str:
        """Converts to a string."""
        rest: str = ""
        if self.next is None:  # Base Case
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"

    # Did in class--returns object as a string (same as function below)


def to_str(head: Node | None) -> str:
    """Show a linked list as a string."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


# Converts values in the linked list to strings (did this in class)

two: Node = Node(2, None)
one: Node = Node(1, two)

print(one)


def last(head: Node) -> int:
    """Return the last value in a non-empty linked list."""
    if head.next is None:  # Base Case
        return head.value
    else:  # Recursive case
        return last(head.next)


# Also done in class: returns the final value in the linked list
# by using head.next to reach the final object and return its value


def recursive_range(start: int, end: int) -> Node | None:
    """Shows recursion of a function through a given range."""
    if start > end:
        raise Exception("Start shouldn't be bigger than end")
    # Base case
    if start == end:
        return None
    # Recursive case
    else:
        first: int = start
        rest: Node | None = recursive_range(start + 1, end)
    return Node(first, rest)


# (In class) If start is greater than end = edge case = raise error
# Base case is when the start node is the same as the end (return none)
# Recursive case: created first variable to plug into the Node parameters at the end
# Used it to get the first value in the linked list
# Used rest to call the function within itself and get the rest of the nodes
# Returned a list of Nodes with first (the start value) as the 1st one
# and rest following it

lots_of_nodes: Node | None = recursive_range(1, 100)
print(lots_of_nodes)
print(last(one))


def value_at(head: Node | None, index: int) -> int:
    """Provides the value for a specific Node."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.value
    else:
        return value_at(head.next, index - 1)


# Was able to raise index error and create base case (index == 0)
# Went to tutoring to clean up the else statement
# Index -1 because we are counting down to the final node in the linked list
# (unlike a regular list which counts up)
# Then call the value_at function at a specific head (counted by the index)


def max(head: Node | None) -> int:
    """Returns the max value in the list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    elif not head.next:
        return head.value
    x: int = max(head.next)
    if head.value > x:
        return head.value
    else:
        return x


# Same value error as above
# Elif statement = if there isn't a new head, return the current one
# Created x to keep track of current max value
# Used another if/else statement to make it replace x if the next
# value was bigger (essentially run through everything and then
# return x if nothing was bigger)


def linkify(items: list[int]) -> Node | None:
    """Returns a linked list of Nodes the same as the original."""
    if not items:
        return None
    return Node(items[0], linkify(items[1:]))


# If statement achieves the same as a value error:
# if the list is empty, return None
# return statement shows it returning a list of Nodes
# with the same values, etc as the original
# by using slice notation (runs through items 1 to the end of the list)
# Can index items (items[0]) because it's a regular list (not linked)


def scale(head: Node | None, factor: int) -> Node | None:
    """Multiplies all Nodes in a linked list by a given factor."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))


# Same as above with if statement
# Similar return statement: use multiplication to scale the first
# value, then call the function and run it through each head
# until everything has been scaled by whatever the factor is
