#!/usr/bin/python3
"""
Module to print a list of all available attr
"""


def lookup(obj):
    """ lookup for all valid attribute """
    return (dir(obj))
