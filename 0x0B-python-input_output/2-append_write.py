#!/usr/bin/python3
"""module to write to a file"""


def append_write(filename="", text=""):
    """ write to a file and print to stdout """
    with open(filename, 'a') as f:
        return f.write(text)
