#!/usr/bin/python3

def no_c(my_string):
    text =""
    for i in my_string:
        if i not in "Cc":
            text += i
    return text
