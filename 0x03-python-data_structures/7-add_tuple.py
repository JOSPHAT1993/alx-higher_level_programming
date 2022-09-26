#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    x = tuple_a[0] + tuple_b[0]
    y = tuple_a[1] + tuple_b[1]

    sum_of_tuples = (x, y)
    return sum_of_tuples
