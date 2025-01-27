#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)  # If the string is empty, return 0 and None
    return (len(sentence), sentence[0])  # Return length and first character

