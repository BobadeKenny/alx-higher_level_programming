#!/usr/bin/python3
"""
This module demonstrates a class MyList that inherits from list
"""


class MyList(list):
    """List Object
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
