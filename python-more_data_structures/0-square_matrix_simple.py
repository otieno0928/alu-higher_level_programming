#!/usr/bin/python3
"""Module that computes the square value of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix."""
    return [[x**2 for x in row] for row in matrix]
