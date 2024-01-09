#!/usr/bin/python3
def no_c(my_string):
    lenghtchar = list(my_string)
    for char in lenghtchar:
        if char == 'c' or char == 'C':
            lenghtchar.remove(char)
    return("".join(lenghtchar))
