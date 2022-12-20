#!/usr/bin/python3
def safe_print_list_intergers(my_list=[], x=0):
    """ function that prints the first x elements of a list and only integers
    Args :
        my_list(list) : list of any type(integers, strings, etc)
        x(int) : number of element to access in the list
    Return :
        real number (int) of integers printed
    """
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
        except (IndexError, TypeError):
            pass
        print("")
    return i
