#!/usr/bin/python3

def best_score(a_dictionary):
    max_value_key = ''
    max_value = -1

    if a_dictionary is None:
        return None

    for k, v in a_dictionary.items():
        if v > max_value:
            max_value = v
            max_value_key = k
    return max_value_key
