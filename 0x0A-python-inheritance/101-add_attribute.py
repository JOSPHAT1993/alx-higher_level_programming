#!/usr/bin/python3
"""101-add_attribute

Todo:
    set an attribute to an obj if not able return exception
"""


def add_attribute(obj, attr, value):
    """adds attirbute"""
    if ('__slots__' in dir(obj) or '__dict__' not in dir(obj) or
            hasattr(obj, attr)):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
