#!/usr/bin/python3
"""
This module implements class Square that
inherits from Rectangle (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class
    """
    def __init__(self, size):
        """initialisation

        Args:
            size (int): size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """string

        Returns:
            str: string representation of class
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
