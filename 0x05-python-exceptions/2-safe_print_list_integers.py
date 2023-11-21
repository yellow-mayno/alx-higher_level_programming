#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for e in my_list:
        if i == x:
            break
        try:
            print("{:d}".format(e), end='\0')
            i = i + 1
        except (TypeError, ValueError):
            pass
    print()
    return (i)
