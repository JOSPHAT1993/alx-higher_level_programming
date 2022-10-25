#!/usr/bin/python3
"""0-read_file

Todo:
    reads a file and prints to stdout
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
