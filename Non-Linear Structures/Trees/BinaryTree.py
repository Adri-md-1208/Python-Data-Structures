"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : binary tree

Description:
    A binary tree is a non-linear data structure that represents nodes connected by edges. Each node
    (called root node) must have as much two edges (called child nodes) that may be roots itself.
    That is a recursive definition of tree.

Operations and asymptotic complexity:
    create_void : returns an empty node. O(1)
    is_void : returns true if the node is empty. O(1)
    get_root : gets the root data. O(1)
    get_right : gets the right child data. O(1)
    get_left : gets the left child data. O(1)
    set_root : sets the root data. O(1)
    set_right : sets the right child data. O(1)
    set_left : sets the left child data. O(1)
    insert_node : inserts a complete node with a root, left child and right child. O(1)
    show_bt : prints all the tree values. O(n^2)

Types supported : all python data types
 """


# IMPLEMENTATION OF BINARY TREE

def create_void():
    """
    :return: empty root node
    """
    return BTree


class BTree:
    def __init__(self, data=None):
        """
        :param data: root data
        """
        self.left = None
        self.right = None
        self.data = data

    def get_root(self):
        """
        :return: right child
        """
        return self.data

    def get_right(self):
        """
        :return: right child
        """
        return self.right

    def get_left(self):
        """
        :return: left child data
        """
        return self.left

    def set_root(self, data):
        """
        :param data: root data to update
        :return: void
        """
        self.data = data

    def set_right(self, right):
        """
        :param right: right child to update
        :return: void
        """
        self.data = right

    def set_left(self, left):
        """
        :param left: left child to update
        :return: void
        """
        self.data = left

    def is_void(self):
        """
        :return: boolean
        """
        return self.data is None

    def insert_node(self, root, lc, rc):
        """
        :param root: root of the node
        :param lc: left child
        :param rc: right child
        :return: void
        """
        self.set_root(root)
        self.left = lc
        self.right = rc

    def show_bt(self):
        """
        :return: void
        """
        print(self.data)
        if self.left:
            self.left.show_bt()
        if self.right:
            self.right.show_bt()
