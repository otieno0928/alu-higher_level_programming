#!/usr/bin/python3
"""Module that safely prints elements of a list."""


def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list on the same line, followed by a new line."""
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
