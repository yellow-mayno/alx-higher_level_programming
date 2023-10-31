#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        pr = ""
        if i % 3 == 0:
            pr = pr + "Fizz"
        if i % 5 == 0:
            pr = pr + "Buzz"
        if i % 5 != 0 and i % 3 != 0:
            pr = i
        print("{} ".format(pr), end='')
