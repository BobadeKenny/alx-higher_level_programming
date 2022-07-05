#!/usr/bin/python3
"""
This module implements class Square that
inherits from Rectangle (9-rectangle.py)
"""


class Student:
    """Square class
    """
    def __init__(self, first_name, last_name, age):
        """initialisation

        Args:
            size (int): size
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """string

        Returns:
            str: string representation of class
        """
        return (self.__dict__)
