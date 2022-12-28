#!/usr/bin/python3
""" Class Module """

class Student:
    """ Student model class"""

    def __init__(self, first_name, last_name, age):
        """ initializing function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Serializing function """
        return self.__dict__
