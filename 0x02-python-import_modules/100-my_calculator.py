#!/usr/bin/python3
import sys

from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    n_args = len(sys.argv) - 1
    if n_args != 3:
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    oprt = sys.argv[2]
    if oprt != '+' and oprt != '-' and oprt != '*' and oprt != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if oprt == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif oprt == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif oprt == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
