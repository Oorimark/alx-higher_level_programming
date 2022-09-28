#!/usr/bin/python3

def uniq_add(my_list=[]):
    summer = 0
    my_list = set(my_list)

    for i in my_list:
        summer = summer + i
    return summer
