#!/usr/bin/python3
"""
This module defines a Square class with area
"""


class Square:
    """Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, size):
        if (type(position) != tuple or len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print('')
        else:
            for i in range(self.position[1]):
                print('')
            for i in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)
