#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new_list = set(my_list)
    my_list = list(new_list)
    for i in range(len(my_list)):
        sum += my_list[i]
    return sum
