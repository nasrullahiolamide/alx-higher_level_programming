#!/usr/bin/python3
""" Save, and update a json file"""

import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# Define all variable needed
arg_d = sys.argv
arg_lst = []
i = 1
filename = "add_item.json"

# check if file exist, if not create a file with empty list
if (not os.path.isfile(filename)):
    save_to_json_file(arg_lst, filename)

# A list of data from the json file
new_lst = load_from_json_file(filename)

# update the list
while i < len(arg_d):
    new_lst.append(arg_d[i])
    i = i + 1

# Dump the list into the json file once again
save_to_json_file(new_lst, filename)
