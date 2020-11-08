"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : set

Description:
    A set is a dynamic data structure that represents a collection of unique.
    The elements are accessed by mapping, like dictionaries. The set data
    structure is predefined by Python.

Operations and asymptotic complexity:
    __init__ : create an empty set. O(1)
    is_empty : returns true if the set is empty. O(1)
    add_element : add an element to the set. O(1)
    remove_element : remove an element of the set. O(n)
    is_in : returns true if the element is in the set. O(n)
    union : returns a new set with the union. O(n)
    intersection : returns a new set with the intersection. O(n)
    difference : returns a new set with the difference. O(n)
    show_set : prints all the elements of the set. O(n)

Types supported :
    The keys must be of an immutable python type (strings, numbers or tuples)
    while the values can be of any predefined data type.

 """

# IMPLEMENTATION OF SET


class _set:
    """
    The _set class is based on <class set> predefined class
    """

    def __init__(self):
        """
        :return: empty set
        """
        self.set = set()

    def is_empty(self):
        """
        :return: boolean
        """
        return not self.set

    def add_element(self, e):
        """
        :param e: element
        :return: None
        """
        self.set.add(e)

    def remove_element(self, e):
        """
        :param e: element
        :return: None
        """
        self.s.discard(e)

    def is_in(self, e):
        """
        :param e: element
        :return: boolean
        """
        return e in self.set

    def union(self, s2):
        """
        :param s2: set 2
        :return: a new set with the union of both sets
        """
        return self.set | s2

    def intersection(self, s2):
        """
        :param s2: set 2
        :return: a new set with the intersection of both sets
        """
        return self.set & s2

    def difference(self, s2):
        """
        :param s2: set 2
        :return: a new set with the difference of s1 with s2
        """
        return self.set - s2

    def show_set(self):
        """
        :return: None (only prints)
        """
        for i in self.set:
            print(i)
