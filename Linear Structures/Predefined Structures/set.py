"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : set

Description:
    A set is a static data structure that represents a collection of immutable items without
    any kind of order. The set data structure is predefined by Python.

Operations and asymptotic complexity:
    create_void : create an empty set. O(1)
    is_void : returns true if the set is empty. O(1)
    add_element : add an element to the set. O(1)
    remove_element : remove an element of the set. O(n)
    is_in : returns true if the element is in the set. O(n)
    union : returns a new set with the union. O(n)
    intersection : returns a new set with the intersection. O(n)
    difference : returns a new set with the difference. O(n)
    show_set : prints all the elements of the set. O(n)

Types supported :
    The keys must be of an immutable python type (strings, numbers or tuples) while the values can
    be of any predefined data type.

 """


# IMPLEMENTATION OF SET

def create_void():
    """
    :return: void set
    """
    return set()


def is_void(s):
    """
    :param s: set
    :return: boolean
    """
    return not s


def add_element(s, e):
    """
    :param s: set
    :param e: element
    :return: void
    """
    s.add(e)


def remove_element(s, e):
    """
    :param s: set
    :param e: element
    :return: void
    """
    s.discard(e)


def is_in(s, e):
    """
    :param s: set
    :param e: element
    :return: boolean
    """
    return e in s


def union(s1, s2):
    """
    :param s1: set 1
    :param s2: set 2
    :return: a new set with the union of both sets
    """
    return s1 | s2


def intersection(s1, s2):
    """
    :param s1: set 1
    :param s2: set 2
    :return: a new set with the intersection of both sets
    """
    return s1 & s2


def difference(s1, s2):
    """
    :param s1: set 1
    :param s2: set 2
    :return: a new set with the difference of s1 with s2
    """
    return s1 - s2


def show_set(s):
    """
    :param s: set
    :return: void (only prints)
    """
    for i in s:
        print(i)
