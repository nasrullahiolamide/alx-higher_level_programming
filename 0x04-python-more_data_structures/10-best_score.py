#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        keys = list(a_dictionary.keys())
        value_list = list(a_dictionary.values())
        max_value = max(value_list)
        for key in keys:
            if a_dictionary[key] == max_value:
                return key
