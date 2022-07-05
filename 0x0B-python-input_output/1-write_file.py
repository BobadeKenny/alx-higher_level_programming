#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str): name of file
        text (str): text to be written

    Returns:
        int: number of characters
    """
    with open(filename, "w", encoding="utf-8") as f:
        num = f.write(text)
    return(num)
