#!/usr/bin/python3
import random
number = random.randit(-10000, 10000)
last = number % 10
if str(number)[0] == "-":
    last = last - 10
if last > 5:
    print("Last digit of", number, 'is',last, "and is greater than 5")
elif last == 0:
    print("List digit of", number, 'is',last, "and is 0")
else:
    print("List digit of", number, 'is',last, "and is less than 6 and not 0")
