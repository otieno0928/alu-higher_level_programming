#!/usr/bin/python3
"""Module that deletes keys with a specific value in a dictionary."""


def complex_delete(a_dictionary, value):
    """Deletes keys having the searched value from the dictionary."""
    if a_dictionary:
        keys_to_delete = [k for k, v in a_dictionary.items() if v == value]
        for key in keys_to_delete:
            del a_dictionary[key]
    return a_dictionary
