#!/usr/bin/python3
"""
    Writes a string to a text file
"""

def write_file(filename="", text=""):
    """open a txt file and if not extist create it"""
    with open(filename, 'w', encoding='utf-8') as file:
               return file.write(text)
