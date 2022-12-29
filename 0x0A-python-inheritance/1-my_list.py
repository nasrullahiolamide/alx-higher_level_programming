#!/usr/bin/python3
"""
print sorted list
"""


class MyList(list):

    def print_sorted(self):
        sorted_list = self.sort()
        print(self)
