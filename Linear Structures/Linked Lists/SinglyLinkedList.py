"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.u3rjc.es
Released under a "GPLv3" license


Data structure : singly linked list (sll)

Description:
    The singly linked list is a linear data structure that is built by nodes. Each node have a data
    property and a next property that aims to the next node.

Operations and asymptotic complexity:
    create_void : create an empty sll. O(1)
    is_void : return true if the sll have no elements. O(1)
    insert_header : insert a node trough the head. O(1)
    insert_tail : appends a node behind the last element. O(n)
    remove_head : removes the header node. O(1)
    remove_element : removes the node that contains that element. O(n)
    first : returns the first element of the sll. O(1)
    last : returns the last element of the sll. O(n)
    show_sll : show all data of the nodes. O(n)


Types supported : all python data types
 """


# IMPLEMENTATION OF SINGLY LINKED LIST

class Node:
    def __init__(self, data=None):
        """
        This constructor creates a unique node with a data associated.
        :param data: element type
        """
        self.data = data
        self.next = None


def create_void():
    """
    :return: void header
    """
    return SinglyLinkedList()


class SinglyLinkedList:
    def __init__(self):
        """
         This constructor creates the header of the sll, which is pointing to a node.
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

    def remove_element(self, data):
        """
        :param data: node that will be removed
        :return: void
        """
        aux = self.head
        i = aux.next

        if (aux is not None) & (aux.data != data):
            while (i.data != data) & (i.next is not None):
                i = i.next
                aux = aux.next
            if i.data == data:
                aux.next = i.next
                i.data = None

    def first(self):
        """
        :return: first element of the sll
        """
        return self.head.data

    def last(self):
        """
        :return: last element of the sll
        """
        i = self.head
        if i is None:
            return None
        else:
            while i.next is not None:
                i = i.next
            return i.data

    def show_sll(self):
        """
        :return: void
        """
        i = self.head
        while i is not None:
            print(i.data)
            i = i.next
