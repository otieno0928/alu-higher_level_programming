#!/usr/bin/python3
"""Module that returns a set of all elements present in only one set."""


def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set."""
    return set_1 ^ set_2
