"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208v
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Algorithm : selection sort

Description:
    The selection sort algorithm selects the minimum value of the array and moves to a sorted array.
    Then repeats the process for each unsorted element in the array.

Algorithmic efficiency : O(n²)
"""


# SELECTION SORT

def selectionSort(array):
    """
    :param array: array of elements
    """
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[min] > array[j]:
                min = j
        array[i], array[min] = array[min], array[i]

lista = [23,54, 6, 2, 12, 79, 122, 67, 21, 16, -1, -12]
selectionSort(lista)
print(lista)
