#!/usr/bin/python3
letter = ""
for i in range(97, 123):
    letter = letter + chr(i)
print("{letter}".format(letter=letter), end='')
