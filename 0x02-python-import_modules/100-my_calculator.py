#!/usr/bin/python3
import calculator_1
from sys import argv, exit

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if op == '+':
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    elif op == '/':
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
