#!/usr/bin/python3
""" OnlySub class  """


def inherits_from(obj, a_class):
    """return if object is an instance of a class"""
    return isinstance(obj, a_class) and type(obj) != a_class
