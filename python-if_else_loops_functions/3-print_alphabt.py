#!/usr/bin/python3
for letter in range(97, 123):
    if letter != 113 and letter != 101:  # ASCII values for 'q' and 'e'
        print("{}".format(chr(letter)), end="")
