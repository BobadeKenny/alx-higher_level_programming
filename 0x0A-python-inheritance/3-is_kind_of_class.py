#!/usr/bin/python3
"""
returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """return True or False

    Args:
        obj (Any): object
        a_class: potential object class instance

    Returns:
        boolean: True or False
    """
    return(isinstance(obj, a_class))
