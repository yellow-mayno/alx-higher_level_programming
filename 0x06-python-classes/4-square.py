#!/usr/bin/python3


class Square:
    """
    empty
    """
    def __init__(self, size=0):
        """
        empty
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        empty
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        empty
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        empty
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
