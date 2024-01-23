#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
    value (int): The printing integer.

    Returns:
    If an Error occurs - then False.
    Otherwise - True.
    """
    try:
        print("{:d}".format(value))
    except:
        return False
    else:
        return True
