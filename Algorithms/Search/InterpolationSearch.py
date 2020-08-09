"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Algorithm : interpolation search

Description:
    The interpolation search algorithm searchs a value in a sorted list using the divide-and-conquer method.
    It searchs in intervals of the array in order to sort the range.

Algorithmic efficiency : O(n) ~ O(log(log n)) depends on the data distribution
"""


# INTERPOLATION SEARCH

def interpolationSearch(array, value):
    """
    :param array: array of elements
    :param value: value to search
    :return: -1 if not founded and index otherwise
    """
    index0 = 0
    indexN = len(array) - 1

    while (index0 <= indexN) and (array[index0] <= value <= array[indexN]):
        mid = index0 + ((indexN - index0) // (array[indexN] - array[index0]) * (value - array[index0]))

        if array[mid] == value:
            return mid

        if array[mid] < value:
            index0 = mid + 1

    return -1

