#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) > 0:
        new_matrix = my_list.copy()
        for i in range(len(new_matrix)):
            if new_matrix[i] == search:
                new_matrix[i] = replace
        return new_matrix
