#!/usr/bin/python3
"""
This module demonstrates an empty class BaseGeometry.
"""


class BaseGeometry:
    """class object
    """
    def area(self):
        """find area

        Raises:
            Exception: area not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate integer

        Args:
            name (str): name of value
            value (any): value to check

        Raises:
            TypeError: value must be an integer
            ValueError: value must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
