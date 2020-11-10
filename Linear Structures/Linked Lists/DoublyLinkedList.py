"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : doubly linked list (dll)

Description:
    The doubly linked list is a linear data structure that is built by nodes.
    Each node have a data property with the node value, a next property that
    aims to the next node and a prev property that aims to the previous node.

Operations and asymptotic complexity (class Node):
    __init__: create an empty node. O(1)
    __repr__: prints the Node info. O(1)

Operations and asymptotic complexity:
    create_void : create an empty dll. O(1)
    is_empty : return true if the dll have no elements. O(1)
    insert_head : insert a node trough the head. O(1)
    insert_tail : appends a node behind the last element. O(n)
    remove_head : removes the header node. O(1)
    remove_element : removes the node that contains that element. O(n)
    head : returns the first element of the dll. O(1)
    tail : returns the last element of the dll. O(n)
    show_dll : show all data of the nodes. O(n)


Types supported : all python data types
 """


# IMPLEMENTATION OF DOUBLY LINKED LIST

class Node:

    def __init__(self, data=None):
        """
        This constructor creates a unique node with a data associated.
        :param data: element type
        :return: None
        """
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        """
        Represent the Node as code
        :return: representation of the Node
        """
        return "< Node (data={self.data} >"


class DoublyLinkedList:

    def __init__(self):
        """
        This constructor creates the header of the dll,
        which is pointing to a node.
        :return: None
        """
        self.head = Node()

    def is_empty(self):
        """
        :return: boolean
        """
        return self.head is None

    def insert_head(self, data):
        """
        :param data: element of the node
        :return: None
        """
        new_head = Node(data)
        new_head.next = self.head
        new_head.prev = None
        if self.is_empty():
            self.head = new_head
        self.head.prev = new_head

    def insert_tail(self, data):
        """
        :param data: element of the node
        :return: None
        """
        if self.head:
            iterator = Node()
            iterator.next = self.head
            while iterator.next:
                iterator = iterator.next
            new_tail = Node(data)
            new_tail.next = None
            new_tail.prev = iterator
            iterator.next = new_tail
        else:
            self.insert_head(data)

    def remove_head(self):
        """
        :return: None
        """
        head_aux = self.head
        self.head = head_aux.next
        head_aux = None
        if self.head:
            self.head.prev = None

    def remove_element(self, data):
        """
        :param data: node that will be removed
        :return: None
        """
        iterator = self.head

        if iterator:
            while (iterator.data != data) & (iterator.next):
                iterator = iterator.next
            if iterator:
                iterator.prev.next = iterator.next
                if iterator.next:
                    iterator.next.prev = iterator.prev
                iterator.data = None

    def head(self):
        """
        :return: first element of the dll
        """
        return self.head.data

    def tail(self):
        """
        :return: last element of the dll
        """
        iterator = self.head
        if iterator:
            while iterator.next:
                iterator = iterator.next
            return iterator.data
        else:
            return None

    def show_dll(self):
        """
        :return: void
        """
        iterator = self.head
        while iterator:
            print(iterator.data)
            iterator = iterator.next
