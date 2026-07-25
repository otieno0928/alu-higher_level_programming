#!/usr/bin/python3
"""
Module defining the MyInt class.
"""


class MyInt(int):
    """
    MyInt class that inherits from int with inverted == and != operators.
    """

    def __eq__(self, other):
        """Invert equality operator == to check inequality."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert inequality operator != to check equality."""
        return super().__eq__(other)
