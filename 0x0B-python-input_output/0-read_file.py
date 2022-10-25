#!/usr/bin/python3
"""0-read_file

Todo:
    reads a file and prints to stdout
"""


def read_file(filename=""):
    """readfile method"""
    with open(filename, mode='r', encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
