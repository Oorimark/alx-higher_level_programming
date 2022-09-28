#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return list(
                map(lambda x: 89 if x == search else x, my_list)
             )
