#!/usr/bin/python3
i = 0
while i < 10:
    j = i + 1
    while j < 10:
        print("{}{}".format(i, j), end=", " if i != 8 or j != 9 else "\n")
        j += 1
    i += 1
