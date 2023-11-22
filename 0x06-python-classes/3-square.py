#!/usr/bin/python3


class Square:
    '''class
    '''
    def __init__(self, size=0):
        '''init
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    '''return
    '''
    def area(self):
        return (self.__size * self.__size)
