#!/usr/bin/python3
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter != 113 and letter != 101:  # ASCII values for 'q' and 'e'
        print("{}".format(letter), end="")
