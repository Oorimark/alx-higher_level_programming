#!/usr/bin/python3

def list_division(list_1, list_2, list_length):
    div_list = list()

    for i in range(list_length):
        try:
            res = float(list_1[i] / list_2[i])
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        div_list.append(res)
    return div_list
