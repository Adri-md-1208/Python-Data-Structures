"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : dictionary

Description:
    A dictionary is a dynamic data structure that is formed by pairs of keys
    and values. The keys are unique while the values may not be.
    The dictionary data structure is predefined by Python.

Operations and asymptotic complexity:
    __init__ : create an empty dictionary. O(1)
    is_empty : return true if the dictionary have no elements. O(1)
    insert_pair : appends a new pair key-value. O(1)
    delete_pair : removes a key-value pair of the dictionary. O(n)
    clear_dict : removes all the key-value pairs of the dictionary. O(n)
    search : search an element and return his value. O(n)
    update : update the value of the key passed. O(n)
    show_dict: show all the key-value pairs of the dictionary. O(n)

Types supported :
    The keys must be of an immutable python type (strings, numbers or tuples)
    while the values can be of any predefined data type.

 """


# IMPLEMENTATION OF DICTIONARY

class _dictionary:
    """
    The _dictionary class is based on <class dict> predefined class
    """

    def __init__(self):
        """
        :return: empty dictionary
        """
        self.dictionary = {}

    def is_void(self):
        """
        :return: boolean
        """
        return not self.dictionary

    def insert_element(self, k, v):
        """
        :param k: key
        :param v: value
        :return: None
        """
        if k not in self.dictionary:
            self.dictionary[k] = v

    def delete_key(self, k):
        """
        :param k: key
        :return: None
        """
        del self.dictionary[k]

    def clear_dict(self):
        """
        :return: None
        """
        self.dictionary.clear()

    def search(self, k):
        """
        :param k: key
        :return: index of the element or -1 in case of no occurrences
        """
        for i in self.dictionary:
            if i == k:
                return self.dictionary[i]
        return -1

    def update(self, k, v):
        """
        :param k: key
        :param v: value
        :return: None
        """
        if k in self.dictionary:
            self.dictionary[k] = v

    def show_dict(self):
        """
        :return: void (only prints)
        """
        for k, v in self.dictionary.items():
            print('{}: {}'.format(k, v))
