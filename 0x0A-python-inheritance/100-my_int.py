#!/usr/bin/python3


class MyInt(int):
    def __init__(self, value):
        self.__value = value
        super().__init__()
    
    def __eq__(self, other):
        self.__other = other
        return self.__value == self.__other
    
    def __ne__(self, other):
        return not self.__eq__(other)

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
