#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = -1 * ((number * (-1)) % 10)
else:
    last = number % 10
# comparaison
if last == 0:
    comp = "and is 0"
elif last > 5:
    comp = "and is greater than 5"
else:
    comp = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, last, comp))
