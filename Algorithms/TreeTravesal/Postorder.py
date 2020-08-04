"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Algorithm : postorder travesal

Description:
    This algorithm traverse all nodes of a tree following the pattern:
    Left --> Right --> Root

Algorithmic efficiency : O(n²)
"""


# POSTORDER TRAVESAL

class BSTree:
    def __init__(self, data=None):
        """
        :param data: root data
        """
        self.left = None
        self.right = None
        self.data = data

    def insert_element(self, data):
        """
        :param data: element to insert
        :return: void
        """
        if not self.data:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = BSTree(data)
                else:
                    self.left.insert_element(data)
            else:
                if self.right is None:
                    self.right = BSTree(data)
                else:
                    self.right.insert_element(data)

    def postorder(self, root):
        """
        :param root: root where start searching
        :return: list with the roots
        """
        postord = []
        if root:
            postord = self.postorder(root.left)
            postord = postord + self.postorder(root.right)
            postord.append(root.data)
        return postord

