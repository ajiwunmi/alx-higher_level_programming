#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """function prints x elements of a list
    Args:
        my_list(list): list of any type (integer, string, etc)
        x(int) : number of elements to be printed
    Returns:
        The number of element printed
    """
    count = 0
    for n in range(x):
        try:

            print("{}".format(my_list[n]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return count
