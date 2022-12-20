#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ function that prints the first x elements of a list and only integers
    Args :
        my_list(list) : list of any type(integers, strings, etc)
        x(int) : number of element to access in the list
    Return :
        real number (int) of integers printed
    """
    i = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            i += 1
    print()
    return i
