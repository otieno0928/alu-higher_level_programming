#!/usr/bin/python3
"""Module containing magic_calculation matching specific Python bytecode."""


def magic_calculation(a, b):
    """Replicates the exact operation sequence of the provided bytecode."""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
        except Exception:
            result = b + a
            break
    return result
