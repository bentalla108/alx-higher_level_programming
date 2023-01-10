#!/usr/bin/python3
"""Script that adds all arguments to a Python list"""
import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

# alternative to check if file exist :os.path.exists(file)
try:
    liste = load_from_json_file(file_name)
except Except:
    liste = []
for argument in argv[1:]:
    liste.append(argument)

save_to_json_file(liste, file_name)
