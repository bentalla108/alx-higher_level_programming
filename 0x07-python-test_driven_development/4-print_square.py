#!/usr/bin/python3
""" Module that print a square with #"""


def print_square(size):

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0 :
        raise ValueError("size must be an integer")

    if not isinstance(size, float) and size < 0 :
        raise TypeError("size must be an integer")
    
    if size == 0 :
        print()
    if size > 0 :
        print(("#" * size + "\n") * size)
