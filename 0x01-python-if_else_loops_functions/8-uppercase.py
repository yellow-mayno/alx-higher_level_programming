#!/usr/bin/python3
# -*- coding: ascii -*-
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            c = ord(i) - 32
        else:
            c = ord(i)
        print("{}".format(chr(c)), end='')
    print("{}".format(""))
