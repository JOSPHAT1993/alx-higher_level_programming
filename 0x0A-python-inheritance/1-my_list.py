#!/usr/bin/python3
"""1-my_list

Todo:
    creates a sub class(Mylist) of class(list)
    prints sorted values in the list
"""
class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """print_sorted method

        Return:
            a sorted list
        """
        print(sorted(self))
