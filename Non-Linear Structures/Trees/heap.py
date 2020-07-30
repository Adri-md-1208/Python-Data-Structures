"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : heap

Description:
    A min heap is a type of tree in which each parent node is less than or equal to its child node.
    A max heap is a type of tree in which each parent node is great than or equal to its child node.
    The heap data structure is implemented by Python's heapq library

Operations and asymptotic complexity: create_void : returns an empty node. O(1)
    create_void : returns an empty list (that represents the nodes). O(1)
    is_void : returns true if the node is empty. O(1)
    insert_element : inserts an element on the heap. O(log n)
    remove_element : removes the less element of the heap. O(n)
    replace_element : removes the less element of the heap and inserts a new element. O(n)
    show_heap : prints all the elements of the heap. O(n)

Types supported : all python data types
"""

import heapq


# IMPLEMENTATION OF HEAP

def create_void():
    """
    :return: void heap
    """
    return []


def is_void(h):
    """
    :param h: heap
    :return: boolean
    """
    return not h


def insert_element(h, e):
    """
    :param h: heap
    :param e: element
    :return: void
    """
    heapq.heappush(h, e)


def remove_element(h):
    """
    :param h: heap
    :return: void
    """
    heapq.heappop(h)


def replace_element(h, e):
    """
    :param h: heap
    :param e: element
    :return: void
    """
    heapq.heapreplace(h, e)


def show_heap(h):
    """
    :param h: heap
    :return: void
    """
    for i in h:
        print(i)
