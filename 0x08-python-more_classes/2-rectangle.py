#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """ Rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of the Rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calcul and Returns the area"""
        return self.__height * self.__width

    def perimeter(self):
        """ Calcul and Returns the perimeter"""
        return (self.__height + self.__width) * 2
