#!/usr/bin/python3
"""Module containing safe integer printing with standard error fallback."""
import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format(), otherwise prints error to stderr."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
