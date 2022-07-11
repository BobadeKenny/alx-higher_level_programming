#!/usr/bin/python3
"""
This class will be the “base” of all other classes in this project
"""


import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return ("[]")
        return(json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON
        string representation json_string
        """
        if json_string is None:
            return []
        return(json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        """
        if list_objs is None:
            dicts = []
        else:
            dicts = [i.to_dictionary() for i in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(Base.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        """
        new_class = cls(1, 1)
        new_class.update(**dictionary)
        return(new_class)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        filename = cls.__name__ + ".json"
        instances = []
        with open(filename, encoding="utf-8") as f:
            json_string = f.read()
            instances = [cls.create(**obj) for obj in cls.from_json_string(json_string)]
        return(instances)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV
        """
        if list_objs is None:
            dicts = []
        else:
            dicts = [i.to_dictionary() for i in list_objs]
        filename = cls.__name__ + ".csv"
        fields = dicts[0].keys()
        with open(filename, "w", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(dicts)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV
        """
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, encoding="utf-8") as f:
            objs = [{key: int(value) for key, value in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)
            ]
        instances = [cls.create(**obj) for obj in objs]
        return(instances)

    @staticmethod
    def draw(list_rectangles, list_squares):
        board = turtle.Turtle()
        for i in (list_rectangles + list_squares):
            board.up()
            board.goto(i.x, i.y)
            board.down()
            board.forward(i.width)
            board.right(90)
            board.forward(i.height)
            board.right(90)
            board.forward(i.width)
            board.right(90)
            board.forward(i.height)
        turtle.done()
