#!/usr/bin/python3
"""7-base_goemetry

Todo:
    Creates a class BaseGeometry
    Within the class create empty method area with exception
    Within the class create a methode integer_validator
"""


class BaseGeometry:
    """BaseGeometry class"""

    def __init__(self):
        """class constructor"""
        pass

    def area(self):
        """area method

        Returns: Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method validating for name and value

        name: str
        value: int
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
