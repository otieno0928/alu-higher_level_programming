#!/usr/bin/python3
"""Module containing a function that executes another function safely."""
import sys


def safe_function(fct, *args):
    """Executes a function safely and captures standard exceptions to stderr."""
    try:
        return fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
