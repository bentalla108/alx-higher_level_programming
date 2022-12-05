#!/usr/bin/python3
def islower(c):
    asc = ord(c)
    if asc in range(ord("a"), ord("z")):
        return True
    else:
        return False
