#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


import json


def load_from_json_file(filename):
    """writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str): name of file
        my_obj (any): object

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        return(json.load(f))
