#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
h1 = repr("holberton")
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
print("Element at index {:d} is {}".format(0, element_at(my_list, 0)))
print("Element at index {:d} is {}".format(-1, element_at(my_list, -1)))
print("Element at index {:d} is {}".format(h1, element_at(my_list, h1)))