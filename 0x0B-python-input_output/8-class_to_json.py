#!/usr/bin/python3
"""
returns an object (Python data structure) represented by a JSON string
"""


def class_to_json(obj):
    """appends a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str): name of file
        text (str): text to be written

    Returns:
        int: number of characters
    """
    return(obj.__dict__)
