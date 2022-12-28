#!/usr/bin/python3
""" Class to json"""

import json


def class_to_json(obj):
    """ the main function """
    return json.dumps(obj.__dict__)
