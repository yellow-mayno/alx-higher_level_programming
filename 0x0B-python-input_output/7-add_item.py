#!/usr/bin/python3
""" dfg sdfg dsf gdsf gdsfg """
import sys
import os.path


sf = __import__('5-save_to_json_file').save_to_json_file
lf = __import__('6-load_from_json_file').load_from_json_file

lst = []
if os.path.exists("add_item.json"):
    lst = lf("add_item.json")

for element in sys.argv[1:]:
    lst.append(element)

sf(lst, "add_item.json")
