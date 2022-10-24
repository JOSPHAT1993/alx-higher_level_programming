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
        if type(value) != int:
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

    def area(self):
        """calculating the area of rectagle"""
        return self.__width * self.__height

    def __str__(self):
        """printing string for rectangle"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """Square class constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """returns string of square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
