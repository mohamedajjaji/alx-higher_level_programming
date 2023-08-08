#!/usr/bin/python3
def fizzbuzz():
    for c in range(1, 101):
        if c % 3 == 0 and c % 5 == 0:
            print("FizzBuzz ".format(c), end='')
        elif c % 3 == 0:
            print("Fizz ".format(c), end='')
        elif c % 5 == 0:
            print("Buzz ".format(c), end='')
        else:
            print("{:d} ".format(c), end='')
