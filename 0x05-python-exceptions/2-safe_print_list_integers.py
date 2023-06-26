#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    int_count = 0
    i = 0
    while i < x:
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=" ")
                int_ count += 1
            i += 1
        except (IndexError, ValueError, TypeError):
            i += 1
            continue
    print()
    return int_count
