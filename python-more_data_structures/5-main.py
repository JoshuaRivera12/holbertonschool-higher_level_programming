#!/usr/bin/pthon3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 12, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))