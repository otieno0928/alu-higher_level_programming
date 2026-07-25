#!/usr/bin/python3
"""Defines a locked class using __slots__."""


class LockedClass:
    """Prevents user from dynamically creating attributes except 'first_name'."""
    __slots__ = ["first_name"]
