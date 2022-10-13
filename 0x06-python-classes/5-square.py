#!/usr/bin/python3
""" 5-square.py
    Class Square with public method (Area)
    Getter - Setter for size attribute
    Print in stdout the square
    Raises:
        TypeError: Error by not be type integer
        ValueError: Error by be negative number
    Returns:
        integer: Square Area (size * size)
"""


class Square():
    """Square Class
    Class Square with public method (Area)
    Getter - Setter for size attribute
    Print in stdout the square
    """

    def __init__(self, size=0):
        """__init__ Constructor
        Contructor with size attribute
        Args:
            size (int, optional): size of Square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """size Getter
        Get size value
        Returns:
            integer: size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size Setter
        Set size value
        Args:
            value (integer): size of Square
        Raises:
            TypeError: Error by not be type integer
            ValueError: Error by be negative number
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """area Method
        Area of Square
        Returns:
            integer: Square Area (size * size)
        """
        return self.__size * self.__size

    def my_print(self):
        """my_print Method
        Prints in stdout the square
        """
        if self.__size == 0:
            print()
            return

        for x in range(self.__size):
            [print("#", end="") for y in range(self.__size)]
            print()
