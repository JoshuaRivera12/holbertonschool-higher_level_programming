#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if i != ord('e') and i != ord('q'):
        print("{}".format(chr(i)), end="")
# The code prints the lowercase alphabet except for 'e' and 'q'
