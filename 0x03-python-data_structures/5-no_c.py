#!/usr/bin/python3
def no_c(my_string):
    list_count_char = list(my_string)
    for char in list_count_char:
        if char == 'c' or char == 'C':
            list_count_char.remove(char)
    return("".join(list_count_char))
