"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208v
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Algorithm : shell sort

Description:
    The shell sort algorithm sorts subarrays of a given array and go on reducing the size of the array until all elements are sorted.

Algorithmic efficiency : O(n²) ~ O(n log²n) depends on gap sequence
"""


# SHELL SORT

def shellSort(array):
    """
    :param array: array of elements
    """
    gap = int(len(array)/2)

    while gap > 0:
        for i in range(gap, len(array)):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j -= gap

            array[j] = temp
        gap = int(gap/2)

lista = [6, 2, 63, 12 ,636 ,-12, 345, -23, -1, 23]
shellSort(lista)
print(lista)
