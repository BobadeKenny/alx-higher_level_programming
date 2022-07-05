#!/usr/bin/python3
"""
a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): name of file

    Returns:
        int: number of characters
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
