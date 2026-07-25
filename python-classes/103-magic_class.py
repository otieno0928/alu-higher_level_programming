#!/usr/bin/python3
"""Module containing MagicClass disassembled from bytecode."""

import math


class MagicClass:
    """Class matching specific bytecode instructions."""

    def __init__(self, radius=0):
        """Initialize MagicClass with radius validation."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate area of the circle."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculate circumference of the circle."""
        return 2 * math.pi * self.__radius
