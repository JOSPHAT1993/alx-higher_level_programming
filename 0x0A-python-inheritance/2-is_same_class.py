#!/usr/bin/python3
"""2-is_same_class

Todo:
    chacking whether an obj is instance of class
"""


def is_same_class(obj, a_class):
    """class checking for type of obj
    and relates with a_class var parsed

    Return:
        True if matches
        False if no match
    """
    if type(obj) == a_class:
        return True
    return False
