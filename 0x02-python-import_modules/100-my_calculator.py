#!/usr/bin/python3
import calculator_1 as calc
import sys

if __name__ == "__main__":
    inputs = sys.argv

    if len(inputs) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op1 = int(inputs[1])
    operator = inputs[2]
    op2 = int(inputs[3])

    if operator == "+":
        print("{:d} + {:d} = {:d}".format(op1, op2, calc.add(op1, op2)))
    elif operator == "-":
        print("{:d} - {:d} = {:d}".format(op1, op2, calc.sub(op1, op2)))
    elif operator == "+":
        print("{:d} * {:d} = {:d}".format(op1, op2, calc.mul(op1, op2)))
    elif operator == "/":
        print("{:d} / {:d} = {:d}".format(op1, op2, calc.div(op1, op2)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
