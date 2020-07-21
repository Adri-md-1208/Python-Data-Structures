"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : tuple

Description:
    A tuple is a dynamic data structure that contains a finite number of immutable elements,
    that can be of different types. The tuple data structure is predefined by Python.

Operations and asymptotic complexity:
    create_void : create an empty tuple. O(1)
    is_void : return true if the tuple have no elements. O(1)
    insert_element : returns a new tuple with the element added. O(n)
    delete_index : returns a new tuple without the element at this index. O(n)
    delete_element : returns a new tuple without the first occurrence of the element. O(n)
    search : search an element and return his index. O(n)
        update : returns a new tuple with the updated element. O(n)
    show_tuple: show all the elements of the tuple. O(n)

Types supported : all python data types
 """


# IMPLEMENTATION OF LIST

def create_void():
    """
    :return: void tuple
    """
    return ()

def is_void(t):
    """
    :param t: tuple
    :return: boolean
    """
    return not t


def insert_element(t, i, e):
    """
    :param t: tuple
    :param i: index
    :param e: element
    :return: new tuple with the element
    """
    return t[:i] + (e,) + t[i:]


def delete_index(t, i):
    """
    :param t: tuple
    :param i: index
    :return: new tuple without the element
    """
    return t[:i] + t[i+1:]


def delete_element(t, e):
    """
    :param t: tuple
    :param e: element
    :return: new tuple without the element
    """
    for i in t:
        if t[i] == e:
            break
    return t[:i] + t[i+1:]


def search(t, e):
    """
    :param t: tuple
    :param e: element
    :return: index of the element or -1 in case of no occurrences
    """
    for i in t:
        if t[i] == e:
            return i
    return -1


def update(t, i, e):
    """
    :param t: tuple
    :param i: index
    :param e: element
    :return: new tuple with the updated element
    """
    return t[:i] + (e,) + t[i+1:]


def show_tuple(t):
    """
    :param t: tuple
    :return: void (only prints)
    """
    for i in t:
        print(i)
