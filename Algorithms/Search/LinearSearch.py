"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Algorithm : linear search

Description:
    The linear search algorithm search over the entire data structure for an element.

Algorithmic efficiency : O(n²)
"""


# LINEAR SEARCH

def linearSearch(array, value):
    """
    :param array: array of elements
    :param value: value to search
    :return: True if the element is found
    """
    i = 0
    found = False
    while (i < len(array)) and not found:
        if array[i] == value:
            found = True
        i += 1
    return found

