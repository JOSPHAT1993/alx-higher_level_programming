#!/usr/bin/python3
"""2-append_write

Todo:
    appending text to a file
"""


def append_write(filename="", text=""):
    """method to append a text"""
    with open(filename, mode='a', encoding="UTF-8") as myFile:
        return myFile.write(text)
