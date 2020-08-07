"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Algorithm : merge sort

Description:
    The merge sort algorithms is based on the divide-and-conquer principle. Consists of spliting the array into halfs and then merge into a sorted array.

Algorithmic efficiency : O(n log n)
"""

import array
typeArray = 'i' # Integer array


# MERGE SORT

def mergeSort(array):
    """
    :param array: array of elements
    :return: array of 1 (or less) element
    """
    if len(array) < 2:
        return array

    mid = int(len(array) / 2)
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    merged = []

    while (len(left) > 0) and (len(right) > 0):
        if left[0] < right[0]:
            merged.append(left[0])
            left.pop(0)
        else:
            merged.append(right[0])
            right.pop(0)

    merged += right
    merged += left
    return merged

lista = [2,45,34,21,5,323,543,66,-12,-34,-3]
lista = mergeSort(lista)
print(lista)








