#!/usr/bin/python3
"""4-rectangle

Todo:
    create private instance width, getter and setter
    create provate instance height, getter and setter
    return area of rectangle.
    return perimeter of the rectangle.
    print perimeter in strings instead of values
"""


class Rectangle:
    """Rectangle class
    """
    def __init__(self, width=0, height=0):
        """class constructor"""
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
        """return area"""
        return (self.width * self.height)

    def perimeter(self):
        """return perimeter of rect"""
        if (self.width == 0 or self.height == 0):
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """modifies string obj"""
        if not self.perimeter():
            return ""
        return ('\n'.join('#' * self.width for i in range(self.height)))

    def __repr__(self):
        """modifies repr obj"""
        return ("Rectangle({}, {})".format(self.width, self.height))
