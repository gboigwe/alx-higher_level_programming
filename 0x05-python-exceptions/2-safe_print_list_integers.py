#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.

    Args:
    my_list (list): Printing elements from.
    x (int): The number of elements of my_list to print.

    Returns:
    Printable element.
    """
    list_count = 0
    try:
        for index in range(x):
            if type(my_list[index]) is int:
                print("{:d}".format(my_list[index]), end="")
                list_count += 1
    except ValueError and TypeError:
        return
    else:
        print()
        return list_count
