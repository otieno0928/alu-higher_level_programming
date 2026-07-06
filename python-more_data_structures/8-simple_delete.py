#!/usr/bin/python3
"""Module that deletes a key in a dictionary."""


def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary if it exists."""
    a_dictionary.pop(key, None)
    return a_dictionary
