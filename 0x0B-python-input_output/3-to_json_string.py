#!/usr/bin/python3
"""
returns the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)

    Args:
        my_obj (any): Object

    Returns:
        str: string representation of obj
    """
    return(json.dumps(my_obj))
