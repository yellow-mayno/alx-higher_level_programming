#!/usr/bin/python3
""" fghd fg hdfgh df """


class Student:
    """ hfg fgh fgh fgh
    """

    def __init__(self, first_name, last_name, age):
        """ gfh gfh fgh fgh fg """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """  fgh fgh fgh fg fgh """
        if type(attrs) == list and attrs is not None:
            temp = {}
            for elem in attrs:
                if type(elem) != str:
                    return self.__dict__
                if elem in self.__dict__.keys():
                    temp[elem] = self.__dict__[elem]
            return temp
        else:
            return self.__dict__
