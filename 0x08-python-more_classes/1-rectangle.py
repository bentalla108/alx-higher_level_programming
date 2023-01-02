#!/usr/bin/python3

class Rectangle:
    """ Rectangle Class"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retunr the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle """
        if not isinstance(value, int):
             raise ValueError("width must be an integer")

        if value < 0 :
            raise ValueError("width must be >= 0")
        
        self.__width = value 

    @property
    def height(self):
        """Retunr the width of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle """
        if not isinstance(value, int):
            raise ValueError("height must be an integer")

        if value < 0 :
            raise ValueError("height must be >= 0")
        
        self.__height = value
