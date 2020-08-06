"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Algorithm : bubble sort

Description:
    The bubble sort algorithm checks every two consecutive elements of the array and sort it.

Algorithmic efficiency : O(n²)
"""


# BUBBLE SORT

def bubbleSort(array):
    """
    :param array: array of elements
    """
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

