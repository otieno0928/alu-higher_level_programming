#!/usr/bin/python3
"""Module that defines a printable Square class."""


class Square:
    """Class defining a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): Size of the square (default 0).
            position (tuple): Tuple of 2 positive integers (default (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get position of square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position of square with validation."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' using position offsets."""
        print(self.__str__(), end="")

    def __str__(self):
        """String representation of a Square instance."""
        if self.__size == 0:
            return ""

        lines = []
        for _ in range(self.__position[1]):
            lines.append("")

        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)
