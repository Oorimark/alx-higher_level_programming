#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            if i < x:
                print(my_list[i], end="")
            else:
                break
        print("")
        return i + 1
    except IndexError as err:
        print("")
        return i
