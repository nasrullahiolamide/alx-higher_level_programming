#!/usr/bin/python3
"""module to print a python object from json"""

import json


def from_json_string(my_str):
    """ convert json to python object """
    return json.loads(my_str)
