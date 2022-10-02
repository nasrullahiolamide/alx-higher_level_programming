#!/usr/bin/python3
"""
No module imported
"""


class Square:
    """
        A class that defines as Square

        -----------
        Private instance attribute: size
        Instantiation with optional size: def __init__(self, size=0):
        Public instance method: def area(self): that returns
        the current square area
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiation with optional size: def __init__(self, size=0)
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        property def size(self) to get the size attribute
        """
        return (self.__size)

    @property
    def position(self):

        return (self.__position)

    @size.setter
    def size(self, value):
        """
        property setter def size(self, value): to update the value of the size
        """
        self.__size = value
        try:
            assert isinstance(value, int)
        except BaseException:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, value):
        """
        to set position, a tuple of two integers
        """
        self.__position = value
        try:
            assert isinstance(value, tuple)
        except BaseException:
            raise TypeError("position must be a tuple of 2 positive integers")
        try:
            assert isinstance(value[0], tuple) or isinstance(value[1], tuple)
        except BaseException:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        public instance method
        returns the current square area
        """
        return (self.__size ** 2)

    def my_print(self, ):
        """
        public instance method
        Method that print a # in size number of times
        """
        if self.size == 0:
            print("")
        else:
            for a in range(self.position[1]):
                print("\n")
            for i in range(self.size):
                for b in range(self.position[0]):
                    print("_", end="")
                for j in range(self.size - 1):
                    print("#", end="")
                print("#")
