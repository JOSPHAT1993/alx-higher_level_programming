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
