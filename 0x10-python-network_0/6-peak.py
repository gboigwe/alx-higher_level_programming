#!/usr/bin/python3
def find_peak(list_of_integers):
    """
        A function that finds peak in a list.
            def find_peak(list_of_integers):
    """
    if not list_of_integers:
        return None
    list_peak = list_of_integers[0]
    for num in list_of_integers:
        if num > list_peak:
            list_peak = num
    return list_peak
