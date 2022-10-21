#!/usr/bin/python3
def print_square(size):
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("Size must be >= 0")
    print('\n'.join("#"*size for i in range(size)))
