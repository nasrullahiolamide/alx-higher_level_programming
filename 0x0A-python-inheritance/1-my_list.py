#!/usr/bin/python3
"""
print sorted list
"""

class MyList(list):
    """"
    My list class
    accepts a list as an argument
    """

    def print_sorted(self):
        """
        Sort function (method)
        """
        print(sorted(self))
