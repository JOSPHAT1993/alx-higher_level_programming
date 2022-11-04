#!/usr/bin/python3
"""Square class

Todo:
    creates the class square.
    calls the super class Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value 
        self.height = value

    def update(self, *args, **kwargs):
        """assigning attributes"""
        if args:
            i = 0
            keys = ['id', 'size', 'x', 'y']

            for arg in args:
                setattr(self, keys[i], args)
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
