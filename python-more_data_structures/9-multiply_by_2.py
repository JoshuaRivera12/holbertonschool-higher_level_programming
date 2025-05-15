#!/usr/bin/python3
def mulitply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.items():
        value * 2
        new_dict[key] = value * 2
    return new_dict
