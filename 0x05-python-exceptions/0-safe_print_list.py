#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
    
    my_list (list): Parameter for elements print.
    x (int): How many elements of my_list to print.

    Returns:
    The printed number of element.
    """
    list_count = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            list_count = list_count + 1
    except:
        print()
        return list_count
    else:
        print()
        return list_count
