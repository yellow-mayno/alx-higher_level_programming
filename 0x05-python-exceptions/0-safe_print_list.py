#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    c = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end='\0')
            c = c + 1
        except (IndexError):
            pass
        i = i + 1
    print()
    return (c)
