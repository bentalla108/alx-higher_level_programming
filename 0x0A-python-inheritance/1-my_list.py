#!/usr/bin/python3
""" MyList """


class MyList(list):
    """prints the list, but sorted (ascending sort)"""

    def print_sorted(self):
        """ Public instance method"""
        print(sorted(self))
