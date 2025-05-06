#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = -last
    if last > 5:
        print(f"Last digit of {number} is {last} and is greater than 5")
    elif last == 0: 
        print(f"Last digit of {number} is {last} and is 0")
    else:
        print(f"Last digit of {number} is {last} and is less than 6 and not 0")
else:
    if last > 5:
        print(f"Last digit of {number} is {last} and is greater than 5")
    elif last == 0:
        print(f"Last digit of {number} is {last} and is 0")
    else:
     print(f"Last digit of {number} is {last} and is less than 6 and not 0")
# The code generates a random integer between -10000 and 10000, calculates its last digit, and prints a message based on the value of the last digit.
            