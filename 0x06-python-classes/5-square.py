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

    def __init__(self, size=0):
        """
        Instantiation with optional size: def __init__(self, size=0)
        """
        self.__size = size

    @property
    def size(self):
        """
        property def size(self) to get the size attribute
        """
        return (self.__size)

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

    def area(self):
        """
        public instance method
        returns the current square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        public instance method
        Method that print a # in size number of times
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for j in range(self.size - 1):
                    print("#", end="")
                print("#")
