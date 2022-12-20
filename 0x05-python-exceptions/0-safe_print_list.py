#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """function prints x elements of a list
    Args :
        my_list(list): list of any type (integer, string, etc)
        x(int) : number of elements to be printed
    Returns
        the number of element printed
    """
    
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            i += 1
        except IndexError:
            break
    print('')
    return i
