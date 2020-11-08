"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : tuple

Description:
    A tuple is an inmutable data structure that contains a finite number of
    immutable elements, that can be of different types.
    The tuple data structure is predefined by Python.

Operations and asymptotic complexity:
    __init__ : create an empty tuple. O(1)
    is_empty : return true if the tuple have no elements. O(1)
    search : search an element and return his index. O(n)
    update : returns a new tuple with the updated element. O(n)
    show_tuple: show all the elements of the tuple. O(n)

Types supported : all python data types
 """


# IMPLEMENTATION OF LIST


class _tuple:
    """
    The _tuple class is based on the <class tuple> predefined class
    """

    def __init__(self):
        """
        :return: empty tuple
        """
        self.tuple = ()

    def is_void(self):
        """
        :return: boolean
        """
        return not self.tuple

    def search(self, e):
        """
        :param e: element
        :return: index of the element or -1 in case of no occurrences
        """
        for i in self.tuple:
            if self.tuple[i] == e:
                return i
        return -1

    def show_tuple(self):
        """
        :return: void (only prints)
        """
        for i in self.tuple:
            print(i)

# TODO: make unitary test
