#!/usr/bin/python3
"""
the class Square that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialisation

        Args:
            id (int): id
            size (int): size
            x (int): x
            y (int): y
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """get size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """set size
        """
        self.width = size
        self.height = size
        self.__size = size

    def __str__(self):
        """string

        Returns:
            str: string representation of class
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x,
                        self.y, self.size))

    def update(self, *args, **kwargs):
        """update square parameters
        """
        if len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if i > 3:
                    break
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """dict representation of rectangle
        """
        to_dict = {
            'id': self.id, 'x': self.x,
            'size': self.size, 'y': self.y}
        return to_dict
