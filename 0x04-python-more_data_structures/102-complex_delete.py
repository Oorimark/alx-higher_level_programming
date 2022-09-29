#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    impure_keys = []

    # select the keys
    for k, v in a_dictionary.items():
        if v == "C":
            impure_keys.append(k)

    # delete keys
    for key in impure_keys:
        del a_dictionary[key]

    return a_dictionary
