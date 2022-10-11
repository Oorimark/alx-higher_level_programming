#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    counter = 0

    try:
        for i in range(x):
            if i < x:
                try:
                    print("{:d}".format(my_list[i]), end="")
                    counter += 1
                except Exception:
                    continue
            else:
                break
        print("")
        return counter
    except Exception as err:
        print("")
        return counter
