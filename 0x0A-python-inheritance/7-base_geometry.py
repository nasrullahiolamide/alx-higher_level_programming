#!/usr/bin/python3
"""
Base Geometry Module
"""


class BaseGeometry(object):
    """
    BaseGeometry Class
    inherits from objects by default
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
