#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        d = fct(*args)
        return d
    except Exception as ex:
        sys.stderr.write("Exception : {}\n".format(ex))
