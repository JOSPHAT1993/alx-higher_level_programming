#!/usr/bin/python3
"""10-student
Todo:
    Create class student
    Instantiate with fname, lname and age.
    define a method returning the class dictionary.
"""


class Student:
    """class stdent"""
    def __init__(self, first_name, last_name, age):
        """class constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """print class dictinary"""
        if (isinstance(attrs, list) and all(
                isinstance(x, str) for x in attrs)):
            return ({x: y for x, y in self.__dict__.items() if x in attrs})
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reloading from json"""
        if (json):
            self.__dict__ = json
