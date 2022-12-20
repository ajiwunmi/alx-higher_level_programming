#!/usr/bin/python3
def safe_print_division(a, b):
    """ function that divides 2 integers and prints the result
    Args:
        a, b (int): interger numbers
    Return:
            The value of the division, otherwise: None
    """
    try:
        result = a / b
    except (ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return(result)
