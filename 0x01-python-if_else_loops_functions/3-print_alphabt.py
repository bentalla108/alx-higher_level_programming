#!/usr/bin/python3
letter = ""
for i in range(ord('a'), ord('z')+1):
    if i == ord('e') or i == ord('q'):
        continue
    letter = letter + chr(i)
print("{letter}".format(letter=letter), end='')
