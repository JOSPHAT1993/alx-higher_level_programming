#!/usr/bin/python3
"""1-write_file

Todo:
    Write to a file.
"""

def write_file(filename="", text=""):
    with open(filename, mode='w', encoding="UTF-8") as f:
        f.write(text)
