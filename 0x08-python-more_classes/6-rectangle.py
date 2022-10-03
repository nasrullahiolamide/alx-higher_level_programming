#!/usr/bin/python3
"""
No imported Module
Module will contain class definition of a rectangle
"""


class Rectangle:
    """
    empty defintion with a pass statement
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializing function with private attribute
        __width and __height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ Method that returns the Rectangle #
        Returns:
            str of the rectangle
        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Method that returns the string represantion of the instance
        Returns:
            string represenation of the object
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
         Method that prints a message when the instance is deleted
        """

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
