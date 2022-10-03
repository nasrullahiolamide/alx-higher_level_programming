#!/usr/bin/python3
"""
No imported Module
Module will contain class definition of a rectangle
"""


class Rectangle:
    """
    empty defintion with a pass statement
    """

    def __init__(self, width=0, height=0):
        """
        Initializing function with private attribute
        __width and __height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate area of a rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        Calculate the perimeter of a rectangle
        """
        if self.width == 0 or self.height == 0:
            return (0)
        else:
            return (2 * (self.width + self.height))
