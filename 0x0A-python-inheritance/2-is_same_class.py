#!/usr/bin/python3
def is_same_class(obj, a_class):
    if type(a_class) is type(obj):
        return True
    return False
