#!/usr/bin/python3

def reducer(func, list_):
    prev, result = 0, 0

    for i in list_:
        result = func(prev, i)
        prev = result
    return result


def weight_average(my_list=[]):
    if not my_list:
        return 0

    mean = reducer(lambda x, y: x + y[1], my_list)
    average = reducer(lambda x, y: x + y, list(
        map(lambda x: x[0] * x[1], my_list))) / mean
    return average
