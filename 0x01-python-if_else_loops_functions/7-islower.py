#!/usr/bin/python3
def islower(c):
    if c in range(97, 123):
        print("{} is lower".format(chr(c)))
    elif c in range(65, 91):
        print("{} is upper".format(chr(c)))