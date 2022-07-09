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

    def __str__(self):
        """string

        Returns:
            str: string representation of class
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x,
                        self.y, self.width))
