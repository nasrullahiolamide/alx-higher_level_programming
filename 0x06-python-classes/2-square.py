#!/usr/bin/python3
"""
No import
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        Initilization function
        """

        self.__size = size
        try:
            isinstance(size, int)

        except BaseException:
            raise TypeError("size must be an Integer")
        if int(size) < 0:
            raise ValueError("size must be >= 0")
