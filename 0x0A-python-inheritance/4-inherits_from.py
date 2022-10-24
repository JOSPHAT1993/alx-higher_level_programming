#!/usr/bin/python3
"""4-inherits_from

Todo:
    checks whether an object has been inherited or not
"""


def inherits_from(obj, a_class):
    """inherits_from class

    Returns: True if inheritance is there otherwise false
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
