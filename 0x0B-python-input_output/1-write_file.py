#!/usr/bin/python3
"""Module that read a file """


def write_file(filename="", text=""):
    """ Read file fonction"""
    with open(filename, 'w', encoding="utf-8") as file:
        file_data = file.write(text)
        file.close()
