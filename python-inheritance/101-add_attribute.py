#!/usr/bin/python3
"""
Module containing the add_attribute function.
"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if possible.
    Raises a TypeError if the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
