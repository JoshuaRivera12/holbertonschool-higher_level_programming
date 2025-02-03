#!user/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # To count the number of integers printed

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Skip non-integer values silently
            continue

    print()  # Move to the next line after printing
    return count
