#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_items = sys.argv

    if (len(arg_items) - 1 == 0):
        print("{:d} arguments.".format(0))
    else:
        if (len(arg_items) - 1 == 1):
            print("{:d} argument:".format(len(arg_items) - 1))
        else:
            print("{:d} arguments:".format(len(arg_items) - 1))
        i = 1
        while i < len(arg_items):
            print("{}: {}".format(i, arg_items[i]))
            i = i + 1
