#!/usr/bin/python3
""" 6-square.py
    Class Square with public method (Area)
    Getter - Setter for size attribute
    Print in stdout the square
    Raises:
        TypeError: Error by not be type integer
        ValueError: Error by be negative number
        TypeError: position must be a tuple of 2 positive integers
    Returns:
        integer: Square Area (size * size)
"""


class Square():
    """Square Class
    Class Square with public method (Area)
    and getter - setter for size attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__ Constructor
        Contructor with size attribute
        Args:
            size (int, optional): size of Square. Defaults to 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position Getter
        Get position valut
        Returns:
            tuple: position square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position Setter
        Set position square
        Args:
            value (tuple): position square
        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

        [print() for i in range(self.__position[1])]

        for x in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for y in range(self.__size)]
            print()
