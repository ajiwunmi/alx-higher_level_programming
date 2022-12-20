#!/usr/bin/python3

def safe_print_integer(value):
    """ prints an integer with "{:d}".format()
    Args:
        value can be interger,string etc
    Returns:
        True or False
    """
    try:
        print("{:d}".format(value))
        status = True
    except (TypeError, ValueError):
        status = False
    return status
