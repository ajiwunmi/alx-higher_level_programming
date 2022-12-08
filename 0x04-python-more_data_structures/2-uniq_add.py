#!/usr/bin/python3
def uniq_add(my_list=[]):
    un_set = set(my_list)
    sum_all = 0
    for i in un_set:
        sum_all += i
    return sum_all
