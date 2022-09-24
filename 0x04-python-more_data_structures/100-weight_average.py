#!/usr/bin/python3

def weight_average(my_list=[]):
    return (my_sum(my_list) / my_weight(my_list))

def my_sum(tuple_list):
    inner_sum = 0
    inner_ps = []
    for x in tuple_list:
        inner_p = x[0] * x[1]
        inner_ps.append(inner_p)
    for i in inner_ps:
        inner_sum = inner_sum + i
    return (inner_sum)

def my_weight(tuple_list):
    weight = 0
    for x in tuple_list:
        weight = weight + x[1]
    return (weight)
