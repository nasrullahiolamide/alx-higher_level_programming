#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    idx = 0
    while new_list[idx] < len(new_list):
        if new_list[idx] == search:
            new_list[idx] = replace
        idx = idx + 1
    return new_list
