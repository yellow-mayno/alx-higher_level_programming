#!/usr/bin/python3
def no_c(my_string):
    lst = list(my_string)
    try:
        lst.remove('c')
        lst.remove('C')
    except ValueError:
        pass
    return ''.join(lst)
