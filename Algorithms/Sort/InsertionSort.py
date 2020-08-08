"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Algorithm : insertion sort

Description:
    The insertion sort algorithm checks the first two elements and sort them, then compare with the third element and sort them again.
    This continue until the array is sorted.

Algorithmic efficiency : O(n²)
"""


# INSERTION SORT

def insertionSort(array):
    """
    :param array: array of elements
    """
    for i in range(len(array)):
        j = i
        while (j > 0)  and (array[j-1] > array[j]):
            array[j], array[j-1] = array[j-1], array[j]
            j = j - 1

lista = [1,4,6,23,3,-12, 8, 14, 2, -2]
insertionSort(lista)
print(lista)
