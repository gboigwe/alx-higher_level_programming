#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely.

    Args:
    fct: The function to execute.
    args: Arguments variable for fct.

    Returns:
    If error - None.
    Otherwise - the result of fct.
    """
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    return result
