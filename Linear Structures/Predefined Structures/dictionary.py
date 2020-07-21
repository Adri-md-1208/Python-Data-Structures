"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : dictionary

Description:
    A dictionary is a dynamic data structure that is formed by pairs of keys and values. The keys are
    unique while the values may not be. The dictionary data structure is predefined by Python.

Operations and asymptotic complexity:
    create_void : create an empty dictionary. O(1)
    is_void : return true if the dictionary have no elements. O(1)
    insert_element : appends a new pair key-value. O(1)
    delete_key : removes a key-value pair of the dictionary. O(n)
    clear_dict : removes all the key-value pairs of the dictionary. O(n)
    delete_dict : removes the entire dictionary. O(n)
    search : search an element and return his value. O(n)
    update : update the value of the key passed. O(n)
    show_dict: show all the key-value pairs of the dictionary. O(n)

Types supported :
    The keys must be of an immutable python type (strings, numbers or tuples) while the values can
    be of any predefined data type.

 """


def create_void():
    """
    :return: void dictionary
    """
    return {}


def is_void(d):
    """
    :param d: dictionary
    :return: boolean
    """
    return not d


def insert_element(d, k, v):
    """
    :param d: dictionary
    :param k: key
    :param v: value
    :return: void
    """
    if not k in d:
        d[k] = v


def delete_key(d, k):
    """
    :param d: dictionary
    :param k: key
    :return: void
    """
    del d[k]


def clear_dict(d):
    """
    :param d: dictionary
    :return: void
    """
    d.clear()


def delete_dict(d):
    """
    :param d: dictionary
    :return: void
    """
    del d


def search(d, k):
    """
    :param d: dictionary
    :param k: key
    :return: index of the element or -1 in case of no occurrences
    """
    for i in d:
        if i == k:
            return d[i]
    return -1


def update(d, k, v):
    """
    :param d: dictionary
    :param k: key
    :param v: value
    :return: void
    """
    if k in d:
        d[k] = v


def show_dict(d):
    """
    :param d: dictionary
    :return: void (only prints)
    """
    for k, v in d.items():
        print(k, ':', v)
