#!/usr/bin/python3
"""Module that returns the weighted average of all integers tuple."""


def weight_average(my_list=[]):
    """Calculates weighted average from a list of tuples."""
    if not my_list:
        return 0

    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    return total_score / total_weight
