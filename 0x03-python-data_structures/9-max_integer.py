#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = -99999
    if my_list == []:
        largest = None
    else:
        for i in range(len(my_list)):
            if my_list[i] > largest:
                 largest = my_list[i]
    return largest
