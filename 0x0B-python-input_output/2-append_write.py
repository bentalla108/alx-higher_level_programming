#!/usr/bin/python3
"""Module that append a file """


def write_file(filename="", text=""):
    """ Read file fonction"""
    with open(filename, 'a', encoding="utf-8") as file:
        file_data = file.write(text)
        file.close()
    return file_data
