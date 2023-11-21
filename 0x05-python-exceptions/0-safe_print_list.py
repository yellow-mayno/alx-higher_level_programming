#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for e in my_list:
            if i == x:
                break
            print("{}".format(e), end='\0')
            i = i + 1
    finally:
        print()
        return (i)
