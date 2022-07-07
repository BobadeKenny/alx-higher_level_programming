#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project
"""


class Base:
    """Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialisation

        Args:
            id (int): id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
