"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : doubly linked list (dll)

Description:
    The doubly linked list is a linear data structure that is built by nodes. Each node have a
    data property, a next property that aims to the next node and a prev property that aims to
    the previous node.

Operations and asymptotic complexity:
    create_void : create an empty dll. O(1)
    is_void : return true if the dll have no elements. O(1)
    insert_header : insert a node trough the head. O(1)
    insert_tail : appends a node behind the last element. O(n)
    remove_head : removes the header node. O(1)
    remove_element : removes the node that contains that element. O(n)
    first : returns the first element of the dll. O(1)
    last : returns the last element of the dll. O(n)
    show_dll : show all data of the nodes. O(n)


Types supported : all python data types
 """


# IMPLEMENTATION OF DOUBLY LINKED LIST

class Node:
    def __init__(self, data=None):
        """
        This constructor creates a unique node with a data associated.
        :param data: element type
        """
        self.data = data
        self.next = None
        self.prev = None


def create_void():
    """
    :return: void header
    """
    return DoublyLinkedList()


class DoublyLinkedList:
    def __init__(self):
        """
         This constructor creates the header of the dll, which is pointing to a node.
        """
        self.head = None

    def is_void(self):
        """
        :return: boolean
        """
        return self.head is None

    def insert_header(self, data):
        """
        :param data: element of the node
        :return: void
        """
        Aux = Node(data)
        Aux.next = self.head
        Aux.prev = None
        if not self.is_void():
            self.head.prev = Aux
        self.head = Aux

    def insert_tail(self, data):
        """
        :param data: element of the node
        :return: void
        """
        if self.head is not None:
            i = Node()
            i.next = self.head
            while i.next is not None:
                i = i.next
            Aux = Node(data)
            Aux.next = None
            Aux.prev = i
            i.next = Aux
        else:
            self.insert_header(data)

    def remove_head(self):
        """
        :return: void
        """
        headAux = self.head
        self.head = headAux.next
        headAux = None
        if self.head is not None:
            self.head.prev = None

    def remove_element(self, data):
        """
        :param data: node that will be removed
        :return: void
        """
        aux = self.head

        if aux is not None:
            while (aux.data != data) & (aux is not None):
                aux = aux.next
            if aux is not None:
                aux.prev.next = aux.next
                if aux.next is not None:
                    aux.next.prev = aux.prev
                aux.data = None

    def first(self):
        """
        :return: first element of the dll
        """
        return self.head.data

    def last(self):
        """
        :return: last element of the dll
        """
        i = self.head
        if i is None:
            return None
        else:
            while i.next is not None:
                i = i.next
            return i.data

    def show_dll(self):
        """
        :return: void
        """
        i = self.head
        while i is not None:
            print(i.data)
            i = i.next
