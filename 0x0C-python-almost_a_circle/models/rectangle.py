#!/usr/bin/python3
"""
the class Rectangle that inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialisation

        Args:
            id (int): id
            width (int): width
            height (int): height
            x (int): x
            y (int): y
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """get width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """set width
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """get heught
        """
        return self.__height

    @height.setter
    def height(self, height):
        """set height
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """get x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """set x
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """get y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """set y
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y