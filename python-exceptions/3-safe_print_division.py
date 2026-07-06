#!/usr/bin/python3
"""Module that safely divides 2 integers."""


def safe_print_division(a, b):
    """Divides 2 integers and prints the result inside a finally block."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
