#!/usr/bin/python3
"""Base Class

Todo:
    define a private class attribute nbobjects
    initialize the class with init method
"""


class Base:
    """class Base"""
    _nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id not None:
            self.id = id
        _nb_objects += 1
        self.id = _nb_objects


