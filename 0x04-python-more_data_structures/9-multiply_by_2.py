#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = dict.copy(a_dictionary)
    for k, v in new_dictionary.items():
        new_dictionary[k] = v * 2
    return new_dictionary
