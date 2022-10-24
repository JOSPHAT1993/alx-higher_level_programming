#!/usr/bin/python3
"""100-my_int

Todo:
    Reverse Equals sign to not equal and vice versa
"""


class MyInt(int):
    """Myint class"""

    def __init__(self, value):
        """Myint class constructor"""
        self.value = value

    def __eq__(self, b):
        """reverse equals to not equals"""
        return self.value != b

    def __ne__(self, b):
        """reverses not equals to equal"""
        return self.value == b
