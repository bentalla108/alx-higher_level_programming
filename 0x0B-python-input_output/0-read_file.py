#!/usr/bin/python3
"""Module that read a file """


def read_file(filename=""):
    """ Read file fonction"""
    with open(filename, 'r', encoding="utf-8") as file:
        file_data = file.read()
        file.close()
    print(file_data, end="")
