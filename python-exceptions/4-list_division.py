#!/usr/bin/python3
"""Module containing a function that divides elements of two lists."""


def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists and handles exceptions."""
    new_list = []
    for i in range(list_length):
        div_res = 0
        try:
            val_1 = my_list_1[i]
            val_2 = my_list_2[i]
            div_res = val_1 / val_2
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div_res)
    return new_list
