#!/usr/bin/python3
"""8-rectangle

Todo:
    Creates a BaseGeormetry class
    creates area method with exception
    creates integer validator method
    creates a subclass rectangle with width and height
"""


class BaseGeometry:
    """BaseGeometry class"""
    def __init__(self):
        """BaseGeometry class constructor"""
        pass

    def area(self):
        """area method raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates name to be an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """subclass Rectangle"""

    def __init__(self, width, height):
        """class rectangle constructor"""
        if not super().integer_validator("width", width):
            self.__width = width
        if not super().integer_validator("height", height):
            self.__height = height
