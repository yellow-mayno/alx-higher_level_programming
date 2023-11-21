#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for e in my_list:
            if i == x:
                break
            print(e, end=" ")
            i = i + 1
        print()
    finally:
        return (i)
