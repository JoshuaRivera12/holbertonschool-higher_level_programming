#!/usr/bin/python3
""" This class sorts all files into a numarical order"""


class MyList(list):
    """this def make the files sorted"""
    def print_sorted(self):
       """this prints the list"""
        print(sorted(self))
