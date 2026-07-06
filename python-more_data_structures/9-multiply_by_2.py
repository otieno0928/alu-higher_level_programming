#!/usr/bin/python3
"""Module that returns a new dictionary with all values multiplied by 2."""


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2."""
    return {key: val * 2 for key, val in a_dictionary.items()}
