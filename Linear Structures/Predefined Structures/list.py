"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : list

Description:
    A list is a dynamic data structure that contains a finite number of
    elements that can be of different types.
    The list data structure is predefined by Python.

Operations and asymptotic complexity:
    __init__ : create an empty list. O(1)
    is_empty : return true if the list have no elements. O(1)
    insert_element : add an element at the index position. O(n)
    append_element : append an element at the last index of the list. O(n)
    delete_index : remove the element at the index position. O(n)
    delete_element : remove the first occurrence of the element. O(n)
    pop_element : remove the last element of the list. O(n)
    search : search an element and return his index. O(n)
    update : change the value of the element at the index position. O(1)
    show_list : show all the elements of the list. O(n)

Types supported : all python types
 """


# IMPLEMENTATION OF LIST


class _list:
    """
    The _list class is based on <class list> predefined class
    """

    def __init__(self):
        """
        :return: empty list
        """
        self.list = []

    def is_empty(self):
        """
        :return: boolean
        """
        return not self.list

    def insert_element(self, i, e):
        """
        :param i: index
        :param e: element
        :return: None
        """
        self.list[i] = e

    def append_element(self, e):
        """
        :param e: element
        :return: None
        """
        self.list.append(e)

    def delete_index(self, i):
        """
        :param i: index
        :return: None
        """
        del self.list[i]

    def delete_element(self, e):
        """
        :param e: element
        :return: None
        """
        self.list.remove(e)

    def pop_element(self):
        """
        :return: None
        """
        self.list.pop()

    def search(self, e):
        """
        :param e: element
        :return: index of the element or -1 in case of no occurrences
        """
        for i in self.list:
            if self.list[i] == e:
                return i
        return -1

    def update(self, i, e):
        """
        :param i: index
        :param e: element
        :return: None
        """
        self.list[i] = e

    def show_list(self):
        """
        :return: void (only prints)
        """
        for i in self.list:
            print(i)
