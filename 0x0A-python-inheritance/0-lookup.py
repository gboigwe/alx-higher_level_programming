#!/usr/bin/python3
""""Defines a function that returns a list"""


def lookup(obj):
    """Function lookup defined
    obj1: created to access the dir of object obj
    Returns the dir of object obj
    """

    obj1 = dir(obj)
    return obj1

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
