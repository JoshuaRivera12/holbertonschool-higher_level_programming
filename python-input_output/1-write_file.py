#!/usr/bin/python3
"""
Writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Opens a text file, creates it if it doesn't exist,
    and writes a string to it.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)

