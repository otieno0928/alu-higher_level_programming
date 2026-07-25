#!/usr/bin/python3
"""Module that defines a Square class with a size attribute."""


class Square:
    """Class that defines a square by size."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the new square.
        """
        self.__size = size
