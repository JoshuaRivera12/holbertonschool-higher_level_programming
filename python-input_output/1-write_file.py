#!/usr/bin/python3
""" This File will write files """


def write_file(filename="", text=""):
    """ this code will write files """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
