#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lst = []
    for i in range(2):
        try:
            lst.append(tuple_a[i])
        except IndexError:
            lst.append(0)
        try:
            lst.append(tuple_b[i])
        except IndexError:
            lst.append(0)
    return (lst[0] + lst[1], lst[2] + lst[3])
