#!/usr/bin/python3
"""
function that appends a string to a text file (UTF8)
and returns the number of characters written
"""


def append_write(filename="", text=""):
    """appends a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str): name of file
        text (str): text to be written

    Returns:
        int: number of characters
    """
    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)
    return(num)
nb_characters_added = append_write("my_first_file.txt", "This School is so cool!\n")
print(nb_characters_added)