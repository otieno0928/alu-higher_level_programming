#!/usr/bin/python3
"""Module defining MyList class that inherits from list."""


class MyList(list):
    """Subclass of list with custom sorting print function."""

    def print_sorted(self):
        """Prints the list in sorted ascending order."""
        print(sorted(self))
