"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Algorithm : binary search

Description:
    In the binary search algorithm we take a sorted array of elements and start looking for the element at the middle. If it
    matches with the searched value the algorithm finish. Otherwise, we repeat the method for the left-half of the elements
    or the right-half depending on the value.

Algorithmic efficiency : O(log n)
"""


# BINARY SEARCH

def binarySearch(array, value):
    """
    :param array: array of elements
    :param value: value to search
    """
    index0 = 0
    indexN = len(array) - 1

    if index0 < indexN:

        mid = (index0 + indexN) // 2

        if array[mid] == value:
            return mid

        elif array[mid] < value:
            index0 = mid + 1

        elif array[mid] > value:
            indexN = mid - 1
    else:
        return None
