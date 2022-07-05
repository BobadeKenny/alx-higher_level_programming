#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


import json


def save_to_json_file(my_obj, filename):
    """writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str): name of file
        my_obj (any): object

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
