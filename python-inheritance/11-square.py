#!/usr/bin/python3
"""Module defining Square class with custom str representation."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class representation."""

    def __init__(self, size):
        """Initialize size after validation."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns string representation of square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
