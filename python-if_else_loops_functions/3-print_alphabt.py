#!/usr/bin/python3
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter != 'e' and letter != 'q':  # ASCII values for 'q' and 'e'
        print("{}".format(letter), end="")
