#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
### Safe print prints the intergers except a character ###
    v = 0
    for i in range(x):
            try:
                print('{:d}'.format(my_list[i]), end="")
                v += 1
            except (ValueError, TypeError):
                continue
            except IndexError:
                break
    print()
    return v
