#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
    my_list_1 (list): First list.
    my_list_2 (list): Second list.
    list_length (int): List length of the two list.

    Returns:
    List length of all the divisions is returned.
    """
    list_len = []
    for i in range(0, list_length):
        try:
            my_list_len = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            list_len.append(my_list_len)
            return (list_len)
