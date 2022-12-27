#!/usr/bin/python3
"""module to write to a file"""


def write_file(filename="", text=""):
    """ write to a file and print to stdout """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
