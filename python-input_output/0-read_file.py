#!/usr/bin/python3
"""
This code will be able to read the content of a txt file
"""


def read_file(filename=""):
    """
    in this code it will print out the content of the file
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
