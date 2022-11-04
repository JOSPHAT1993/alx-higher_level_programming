#!/usr/bin/python3
"""Rectangle Class

Todo:
    create a class rectangle,
    The class inherits from Base Class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class contructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def validation_method(self, name, value):
        """validates the getters and setter methods"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if ((name is "width") or (name is "height")) and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if ((name is "x" or name is "y") and value < 0):
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.validation_method("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.validation_method('height', value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.validation_method('x', value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.validation_method('y', value)
        self.__y = value

    def area(self):
        """area method"""
        return (self.width * self.height)

    def display(self):
        """displays rectangle using # chars"""
        print('\n' * self.y, end="")
        print(''.join(' ' * self.x + '#' * self.width + '\n'
                      for x in range(self.height)), end="")

    def __str__(self):
        """returning string"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def update(self, *args):
        """add an argument to each attribute"""
        i = 0
        keys = ['id', 'width', 'height', 'x', 'y']
        for x in args:
            setattr(self, keys[i], args)
            i += 1
