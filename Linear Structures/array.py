"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : array
Description:
    An array is a dynamic data structure that contains a finite number of elements that are all of the
    same type (numeric only). The array type is predefined by Python and we do not have to implement it.
Operations and asymptotic complexity:
    create_void : create an empty array. O(1)
    is_void : returns if the array have no elements. O(1)
    insert_element : add an element at the index position. O(1)
    delete_index : remove the element at the index position. O(1)
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

from array import *


# IMPLEMENTATION OF ARRAY

def create_void(t):
    """
    :param t: type of the elements (string)
    :return: void array
    """
    return array(t, [])


def is_void(a):
    """
    :param a: array
    :return: boolean
    """
    if a.buffer_info()[1] == 0:
        return True
    return False


def insert_element(a, i, e):
    """
    :param a: array
    :param i: index
    :param e: element
    :return: void
    """
    a.insert(i, e)


def delete_index(a, i):
    """
    :param a: array
    :param i: integer
    :return: void
    """
    a.pop(i)


def delete_element(a, e):
    """
    :param a: array
    :param e: element
    :return: void
    """
    a.remove(e)


def search(a, e):
    """
    :param a: array
    :param e: element
    :return: index of the element or -1 in case of no occurrences
    """
    for i in a:
        if a[i] == e:
            return i
        return -1


def update(a, i, e):
    """
    :param a: array
    :param i: index
    :param e: element
    :return: void
    """
    a[i] = e


def show_array(a):
    """
    :param a: array
    :return: void (only prints)
    """
    for i in a:
        print(i)
