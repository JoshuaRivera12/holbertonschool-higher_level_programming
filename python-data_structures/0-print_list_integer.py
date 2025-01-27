#!bin/user/python3

def print_list_integer(my_list=[]):
    for i in my_list:
        # Use str.format() to print each integer
        print("{:d}".format(i))

