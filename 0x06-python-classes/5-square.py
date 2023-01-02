#!/usr/bin/python3
"""Defines the class square"""


class Square:
    """The sqaure"""

    def __init__(self, size=0):
        """Initialise a new square

        Args:
            size(int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with # character"""
        for a in range(0, self.__size):
            [print("#", end="") for n in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")