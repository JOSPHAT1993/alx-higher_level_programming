#!/usr/bin/python3
"""9-student

Todo:
    Create class Student
    instantiate the class with fname, lname and age (public)
    define a method for retrieving dictionary repre.
"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """class costructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returning a class disctionary"""
        return self.__dict__
