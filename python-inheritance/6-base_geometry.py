#!/usr/bin/python3
"""Module defining BaseGeometry with unimplemented area method."""


class BaseGeometry:
    """BaseGeometry class with area method."""

    def area(self):
        """Raises Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
