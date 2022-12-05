#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    for i in my_list:
        if idx < 0:
            return
        if idx > length - 1:
            return
        return(my_list[idx])
