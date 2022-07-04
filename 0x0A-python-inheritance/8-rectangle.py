#!/usr/bin/python3
"""
This module demonstrates a rectangle class
based on BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class
    """
    def __init__(self, width, height):
        """initialisation

        Args:
            width (int): width
            height (int): height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
