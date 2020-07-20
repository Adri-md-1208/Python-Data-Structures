"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : list

Description:
    A list is a dynamic data structure that contains a finite number of elements that can be of different types.
    The list data structure is predefined by Python.

Operations and asymptotic complexity:
    create_void : create an empty list. O(1)
    is_void : return true if the list have no elements. O(1)
    insert_element : add an element at the index position. O(n)
    delete_index : remove the element at the index position. O(n)
    delete_element : remove the first occurrence of the element. O(n)
    search : search an element and return his index. O(n)
    update : change the value of the element at the index position. O(1)
    show_list : show all the elements of the list. O(n)

Types supported : all python data types
 """


# IMPLEMENTATION OF LIST

def create_void():
    """
    :return: void list
    """
    return []


def is_void(l):
    """
    :param l: list
    :return: boolean
    """
    return not l


def insert_element(l, i, e):
    """
    :param l: list
    :param i: index
    :param e: element
    :return: void
    """
    l.insert(i, e)


def delete_index(l, i):
    """
    :param l: list
    :param i: index
    :return: void
    """
    del l[i]


def delete_element(l, e):
    """
    :param l: list
    :param e: element
    :return: void
    """
    l.remove(e)


def search(l, e):
    """
    :param l: list
    :param e: element
    :return: index of the element or -1 in case of no occurrences
    """
    for i in l:
        if l[i] == e:
            return i
    return -1


def update(l, i, e):
    """
    :param l: list
    :param i: index
    :param e: element
    :return: void
    """
    l[i] = e


def show_list(l):
    """
    :param l: list
    :return: void (only prints)
    """
    for i in l:
        print(i)
