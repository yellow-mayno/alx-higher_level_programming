#!/usr/bin/python3
"""empty"""

class Square:
    """empty"""
    
    def __init__(self, size=0):
        """empty
        
        Args:
            size (int): lkjlkjlk
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
