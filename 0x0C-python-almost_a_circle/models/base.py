#!/usr/bin/python3
<<<<<<< HEAD
"""Base class module"""
import json
import csv
import turtle as t
import time
from random import randrange

class Base():
    """Base class"""
    ___nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.___nb_objects += 1
            self.id = Base.___nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string rep of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string rep of list_objs to .json file"""
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns a list of dictionaries from json string"""
        if json_string is None or not json_string:
=======
"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.
        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
>>>>>>> 0068b829556d7b7d47bb16d0818ea327cd4228fa
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
<<<<<<< HEAD
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """loads instance attributes from .json file and creates instances"""
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                return [cls.create(**i) for i in
                        cls.from_json_string(f.read())]
        except FileNotFoundError:
=======
        """Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
>>>>>>> 0068b829556d7b7d47bb16d0818ea327cd4228fa
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
<<<<<<< HEAD
        """writes list_objs to csv file"""
        if list_objs is not None:
            if cls.__name__ == "Rectangle":
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            elif cls.__name__ == "Square":
                list_objs = [[o.id, o.size, o.x, o.y] for o in list_objs]
            with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """loads instance attributes from csv file and creates instances"""
        ret = []
        try:
            with open(cls.__name__ + ".csv", "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for obj in reader:
                    v = [eval(i) for i in obj]
                    if cls.__name__ == "Rectangle":
                        dct = {"id": v[0], "width": v[1], "height": v[2],
                               "x": v[3], "y": v[4]}
                    elif cls.__name__ == "Square":
                        dct = {"id": v[0], "size": v[1], "x": v[2], "y": v[3]}
                    ret.append(cls.create(**dct))
            return ret
        except FileNotFoundError:
            return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        # draw a starting point some dist from the window corner
        # In this grid: down is +ve y-axis and right is +ve x-axis
        t.bgcolor("green")
        t.color("red")
        t.clear()
        t.up()
        w_h = t.window_height()
        w_w = t.window_width()
        center = -(w_w/2 - 20), (w_h/2 - 20)
        l = w_w * 0.7
        s = 20
        t.setpos(center)        #+ve x
        t.down()
        t.forward(l)
        t.left(90)
        t.setpos(center)        #-ve y
        t.forward(s)
        t.left(90)
        t.setpos(center)        #-ve x
        t.forward(s)
        t.left(90)
        t.setpos(center)        #+ve y
        t.forward(l)
        t.left(90)
        t.up()
        t.setpos(center)

        # draw given rectangles and squares
        t.colormode(255)
        for i in list_rectangles + list_squares:
            try:
                h = i.size
                w = i.size
            except AttributeError:
                h = i.height 
                w = i.width
            x = i.x
            y = i.y
            t.color("orange")
            t.fillcolor(randrange(256), randrange(256), randrange(256))
            t.begin_fill()
            t.up()
            t.setpos(center[0] + x, center[1] - y)
            t.down()
            t.pensize(1)
            t.seth(0)
            t.forward(w)
            t.right(90)
            t.forward(h)
            t.right(90)
            t.forward(w)
            t.right(90)
            t.forward(h)
            t.right(90)
            t.end_fill()
        time.sleep(20)           # delay for 10 secs
        t.bye()                  # close window
=======
        """Write the CSV serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.
        Reads from `<cls.__name__>.csv`.
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
>>>>>>> 0068b829556d7b7d47bb16d0818ea327cd4228fa
