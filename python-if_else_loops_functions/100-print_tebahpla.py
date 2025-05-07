#!/usr/bin/python3
i = 122
toggle = 0
while i >= 97:
    if toggle == 0:
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(i).upper()), end="")
    toggle = 1 - toggle
    i -= 1
