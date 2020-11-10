"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : singly linked list (sll)

Description:
    The singly linked list is a linear, dynamic data structure that is built
    by nodes. Each node have a data property with the value of the node and
    a next property that aims to the next node.

Operations and asymptotic complexity (class Node):
    __init__: create an empty node. O(1)
    __repr__: prints the Node info. O(1)

Operations and asymptotic complexity (class SinglyLinkedList):
    __init__ : create an empty sll. O(1)
    is_empty : return true if the sll have no elements. O(1)
    insert_head : insert a node trough the head. O(1)
    insert_tail : appends a node behind the last element. O(n)
    remove_head : removes the header node. O(1)
    remove_element : removes the node that contains that element. O(n)
    head : returns the first element of the sll. O(1)
    tail : returns the last element of the sll. O(n)
    show_sll : show all data of the nodes. O(n)


Types supported : all python data types
 """


# IMPLEMENTATION OF SINGLY LINKED LIST

class Node:

    def __init__(self, data=None):
        """
        This constructor creates an unique node with the data property.
        :param data: element
        :return: None
        """
        self.data = data
        self.next = None

    def __repr__(self):
        """
        Represent the Node as code
        :return: representation of the Node
        """
        return "< Node (data={self.data} >"


class SinglyLinkedList:

    def __init__(self):
        """
        This constructor creates the header of the sll,
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
        self.head = new_head

    def insert_tail(self, data):
        """
        :param data: element of the node
        :return: None
        """
        if self.head is not None:
            iterator = Node()
            iterator.next = self.head
            while iterator.next:
                iterator = iterator.next
            new_tail = Node(data)
            new_tail.next = None
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

    def remove_element(self, data):
        """
        :param data: node that will be removed
        :return: None
        """
        iterator = self.head
        next_iter = iterator.next

        if (iterator is not None) & (iterator.data != data):
            while (next_iter.data != data) & (next_iter.next):
                next_iter = next_iter.next
                iterator = iterator.next
            if next_iter.data == data:
                iterator.next = next_iter.next
                next_iter.data = None

    def head(self):
        """
        :return: first element of the sll
        """
        return self.head.data

    def tail(self):
        """
        :return: last element of the sll
        """
        if self.head is None:
            return None
        else:
            iterator = self.head
            while iterator.next:
                iterator = iterator.next
            return iterator.data

    def show_sll(self):
        """
        :return: None
        """
        iterator = self.head
        while iterator:
            print(iterator.data)
            iterator = iterator.next
