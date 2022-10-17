#!/usr/bin/python3
"""3-rectangle

Todo:
    creating class Rectangle.
    Creating private instance width, getters and setters.
    Creating private instance height, getters and setters.
    Finding Area and Perimeter.
"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """Class Constructor"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """height getter"""
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
        """width getter"""
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
        """Area calculation"""
        return (self.width * self.height)

    def perimeter(self):
        """Perimeter Calculation"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """prints alternate
        """
        if not self.perimeter():
            return ""
        return ('\n'.join('#' * self.width for x in range(self.height)))
