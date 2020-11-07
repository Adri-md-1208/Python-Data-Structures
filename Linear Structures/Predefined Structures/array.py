"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : array

Description:
    An array is a dynamic data structure that contains a finite number of
    elements that are all of the same type (numeric only).
    The array type is predefined by Python.

Operations and asymptotic complexity:
    __init__ : create an empty array. O(1)
    is_empty : return true if the array have no elements. O(1)
    insert_element : add an element at the index position. O(n)
    delete_index : remove the element at the index position. O(n)
    delete_element : remove the first occurrence of the element. O(n)
    search : search an element and return his index. O(n)
    update : change the value of the element at the index position. O(1)
    show_array : show all the elements of the array. O(n)

Types supported (most common):
    b : signed integer of 1 byte
    B : unsigned integer of 1 byte
    i : signed integer of 2 bytes
    I : unsigned integer of 2 bytes
    f : float of 4 bytes
    d : double of 8 bytes
"""

from array import array

# IMPLEMENTATION OF ARRAY


class _array:
    """
    The _array class is based on <class array.array> predefined class
    """

    def __init__(self, t):
        """
        :param t: type of the elements (string)
        :return: empty array
        """
        self.array = array(t, [])

    def is_empty(self):
        """
        :return: boolean
        """
        if self.array.buffer_info()[1] == 0:
            return True
        return False

    def insert_element(self, i, e):
        """
        :param i: index
        :param e: element
        :return: None
        """
        self.array.insert(i, e)

    def delete_index(self, i):
        """
        :param i: index
        :return: None
        """
        self.array.pop(i)

    def delete_element(self, e):
        """
        :param e: element
        :return: None
        """
        self.array.remove(e)

    def search(self, e):
        """
        :param e: element
        :return: index of the element or -1 in case of no occurrences
        """
        for i in self.array:
            if i == e:
                return i
        return -1

    def update(self, i, e):
        """
        :param i: index
        :param e: element
        :return: None
        """
        self.array[i] = e

    def show_array(self):
        """
        :return: void (only prints)
        """
        for i in self.array:
            print(i)

# TODO : Make unit test
