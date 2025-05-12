#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    args = [tuple_a, tuple_b]
    for i in range(2):
        if len(args[i]) < 2:
            args[i] = args[i] + (0,) * (2 - len(args[i]))
    return (args[0][0] + args[1][0], args[0][1] + args[1][1])