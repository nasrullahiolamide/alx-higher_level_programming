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
        self.size = size
        self.position = position

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
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        public instance method
        returns the current square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
