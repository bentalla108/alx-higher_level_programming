#!/usr/bin/python3
<<<<<<< HEAD
"""Rectangle class module"""
=======
"""Defines a rectangle class."""
>>>>>>> 0068b829556d7b7d47bb16d0818ea327cd4228fa
from models.base import Base


class Rectangle(Base):
<<<<<<< HEAD
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
=======
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
>>>>>>> 0068b829556d7b7d47bb16d0818ea327cd4228fa
        self.width = width
        self.height = height
        self.x = x
        self.y = y
<<<<<<< HEAD

    def validate(self, name, value):
        """validates all values"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif (name == "x" or name == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def x(self):
        """rectangle's x pos"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """rectangle's y pos"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate("y", value)
        self.__y = value

    @property
    def width(self):
        """rectangle's width"""
=======
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the Rectangle."""
>>>>>>> 0068b829556d7b7d47bb16d0818ea327cd4228fa
        return self.__width

    @width.setter
    def width(self, value):
<<<<<<< HEAD
        self.validate("width", value)
=======
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
>>>>>>> 0068b829556d7b7d47bb16d0818ea327cd4228fa
        self.__width = value

    @property
    def height(self):
<<<<<<< HEAD
        """rectangle's height"""
=======
        """Set/get the height of the Rectangle."""
>>>>>>> 0068b829556d7b7d47bb16d0818ea327cd4228fa
        return self.__height

    @height.setter
    def height(self, value):
<<<<<<< HEAD
        self.validate("height", value)
        self.__height = value

    def area(self):
        """returns area of this rectangle"""
        return self.width * self.height

    def display(self):
        """Prints rectangle instance with the character #"""
        rec_s = "\n" * self.y + (" " * self.x + "#" * self.width +
                                 "\n") * self.height
        print(rec_s, end="")

    def __str__(self):
        """returns a string rep of this rectangle"""
        return "[{}] ({}) {}/{} - {}/{}"\
            .format(type(self).__name__, self.id, self.x, self.y,
                    self.width, self.height)

    def __updArgsKwarg(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method for updating the square"""
        args = locals()
        for k in args.keys():
            if args[k] is not None and k != "self" and k == "id":
                self.__dict__[k] = args[k]
            elif args[k] is not None and k != "self":
                self.__dict__["_" + type(self).__name__ + "__" + k] = args[k]

    def update(self, *args, **kwargs):
        """Updates the square"""
        if args:
            self.__updArgsKwarg(*args)
        elif kwargs:
            self.__updArgsKwarg(**kwargs)

    def to_dictionary(self):
        """returns a dictionary rep of this rectangle"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
=======
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
>>>>>>> 0068b829556d7b7d47bb16d0818ea327cd4228fa
