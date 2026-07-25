#!/usr/bin/python3
"""Module checking class instance or inheritance."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance or inherited instance of a_class."""
    return isinstance(obj, a_class)
