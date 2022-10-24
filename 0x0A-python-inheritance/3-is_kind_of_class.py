#!/usr/bin/python3
"""3-is_kind_of_class

Todo:
    check whether an object is an instance of
"""


def is_kind_of_class(obj, a_class):
    """chacks for instance of

    Returns: True if is instance of the class otherwise false
    """
    if isinstance(obj, a_class):
        return True
    return False
