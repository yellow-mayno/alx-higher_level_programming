#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -1 * number
    r = number % 10
    print(r, end='')
    return r
