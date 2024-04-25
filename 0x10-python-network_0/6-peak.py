#!/usr/bin/python3
"""
    ALX SE Technical interview preparation
    A function that finds the highest number
    in the list of unsorted integers
"""


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



def find_peak(list_of_integers):
    """
        A function that finds peak in a list.
            def find_peak(list_of_integers):
    """
    if not list_of_integers:
        return None

    least = 0
    peak = len(list_of_integers) - 1

    while least < peak:
        temp = (least + peak) // 2

        if list_of_integers[temp] < list_of_integers[temp + 1]:
            least = temp + 1
        else:
            peak = temp

    return list_of_integers[least]
