#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0:
        return None
    elif idx > length - 1:
        return None
    elif idx >= 0 and idx <= len(my_list):
        return my_list[idx]
    else:
        return None
