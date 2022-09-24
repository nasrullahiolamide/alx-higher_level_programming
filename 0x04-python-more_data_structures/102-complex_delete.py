#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = get_key(a_dictionary, value)
    if keys:
        for i in keys:
            del a_dictionary[i]
        return a_dictionary
    else:
        return a_dictionary

def get_key(a_dictionary, x):
    values = list(a_dictionary.values())
    idx = 0
    list_of_keys = []
    while idx < len(values):
        if values[idx] == x:
            key = list(a_dictionary.keys())[idx]
            list_of_keys.append(key)
        idx = idx + 1
    return (list_of_keys)
