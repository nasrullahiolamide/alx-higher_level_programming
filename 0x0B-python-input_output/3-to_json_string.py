#!/usr/bin/python3
"""module to write to a file"""

import json


def to_json_string(my_obj):
    """ write to a file and print to stdout """
    return json.dumps(my_obj)
