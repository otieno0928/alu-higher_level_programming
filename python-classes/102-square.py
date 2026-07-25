#!/usr/bin/python3
"""Module defining a Square class with comparison capability."""


class Square:
    """Class defining a square with comparative operators."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int/float): Size of square (default 0).
        """
        self.size = size

    @property
    def size(self):
        """Get size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of square with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if self area equals other area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if self area is not equal to other area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if self area is less than other area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if self area is less than or equal to other area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if self area is greater than other area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if self area is greater than or equal to other area."""
        return self.area() >= other.area()
