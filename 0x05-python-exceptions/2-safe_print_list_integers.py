#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='\0')
        except (TypeError, ValueError):
            pass
        i = i + 1
    print()
    return (i)
