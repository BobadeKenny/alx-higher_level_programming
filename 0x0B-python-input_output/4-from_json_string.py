#!/usr/bin/python3
"""
returns an object (Python data structure) represented by a JSON string
"""

import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (str): JSON string

    Returns:
        object: Python data structure
    """
    return(json.loads(my_str))
