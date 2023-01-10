#!/usr/bin/python3
"""Module returns the JSON representation """
import json


def to_json_string(my_obj):
    """Method that returns the JSON representation of an object"""
    return json.dumps(my_obj)
