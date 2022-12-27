#!/usr/bin/python3
"""module to create a python object from json"""

import json


def load_from_json_file(filename):
    """ obj from json """
    with open(filename, 'r') as f:
        return json.load(f)
