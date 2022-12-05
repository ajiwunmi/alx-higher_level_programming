#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < 0:
        return(my_list)
    length = len(my_list)
    if idx > length:
        return(my_list)

    for i in range(length):
        if i == idx:
            new_list[i] = element

    return(new_list)
