#!/usr/bin/python3
"""Module for appending a string to the end of a text file."""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
