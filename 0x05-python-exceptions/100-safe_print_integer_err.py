#!/usr/bin/python3
def safe_print_integer_err(value):
    """ function that prints an integer
        Args: value can be any type (integer, string)
    """
    import sys
    try:
        print("{:d}".format(value))
        status = True
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        status = False
        
    return(status)
