#!/usr/bin/python3
"""
returns True if the object is exactly an instance of the specified class;
otherwise False
"""


def is_same_class(obj, a_class):
    """return True or False

    Args:
        obj (Any): object
        a_class: potential object class

    Returns:
        boolean: True or False
    """
    return (type(obj) == a_class)
