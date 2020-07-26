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
    create_void : returns an empty node
    is_void : returns true if the node is empty
    insert_node : inserts a complete node with a root, left child and right child

Types supported : all python data types
 """


# IMPLEMENTATION OF BINARY TREE

def create_void():
    """
    :return: empty root node
    """
    return Node


class Node:
    def __init__(self, data):
        """
        Constructor for each node
        :param data: the data of the node
        """
        self.left = None
        self.right = None
        self.data = data


class BTree:
    def __init__(self):
        self.root = None

    def is_void(self):
        """
        :return: boolean
        """
        return self.root is None

    def insert_node(self, root, lc, rc):
        """
        :param root: root of the node
        :param lc: left child
        :param rc: right child
        :return: void
        """
        self.root.data = root
        self.root.left = Node(lc)
        self.root.right = Node(rc)
