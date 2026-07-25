#!/usr/bin/python3
"""Defines a locked class using __slots__."""


class LockedClass:
    """Prevents setting attributes other than 'first_name'."""

    __slots__ = ["first_name"]
