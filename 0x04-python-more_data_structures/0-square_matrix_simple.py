#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    return list(
                map(lambda list: [x*x for x in list], matrix)
            )
