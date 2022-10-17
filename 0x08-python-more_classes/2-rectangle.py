#!/usr/bin/python3
"""2-rectangle

Todo:
    create private attribute width, getters and setters.
    create private attribute height, getters and setters.
    Returns Area method for Rectangle.
    Returns Perimeter Method for the Rectangle.
"""


class Rectangle:
    """Rectangle class
    """
    def __init__(self, width=0, height=0):
        """Class constructor"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """height getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Area Calculation"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter Calculation"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))
