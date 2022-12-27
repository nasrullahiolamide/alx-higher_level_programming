#!/usr/bin/python3
"""module to save a json representation of py to file"""

import json


def save_to_json_file(my_obj, filename):
    """ save to json file """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
