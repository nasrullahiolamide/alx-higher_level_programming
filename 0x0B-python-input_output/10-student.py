#!/usr/bin/python3
""" Class Module """


class Student:
    """ Student model class"""

    def __init__(self, first_name, last_name, age):
        """ initializing function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Serializing function """
        new_dict = {}

        # covert dict rep into list of tuples
        for key, value in self.__dict__.items():
            # chck if attr list is empty to return original dict
            if (isinstance(attrs, list) and len(attrs) == 0):
                return new_dict
            elif (not attrs):
                return self.__dict__
            else:
                # loop over attr to check if it matches the key
                # to return modified dict
                for attr in attrs:
                    if attr in key:
                        new_dict[attr] = value

        self.__dict__ = new_dict

        return self.__dict__
