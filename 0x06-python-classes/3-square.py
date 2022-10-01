#!/usr/bin/python3

class Square:

    def __init__(self, size):
        """
        private instance attribute
        parameters
        ------------------
        size : integer else TypeError
        if size less than 0, raise value error
        """
        self.__size = size
        try:
            assert isinstance(size, int)
        except BaseException:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)
