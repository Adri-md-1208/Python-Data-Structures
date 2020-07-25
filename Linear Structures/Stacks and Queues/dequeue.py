"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : dequeue

Description:
    The dequeue data structure is a predefined data structure from the collections module. Is a queue
    that supports adding and removing elements from either ends. Is a FIFO structure.

Operations and asymptotic complexity:
    create_void : create an empty dequeue. O(1)
    is_void : return true if the dequeue have no elements. O(1)
    push_right : insert a element in the right-end. O(n)
    push_left : insert a element in the left-end. O(1)
    pop_right : removes the right-end element of the dequeue. O(n)
    pop_left : removes the left-end element of the dequeue. O(n)
    peek_right : returns the right-peek element of the dequeue (the last). O(n)
    peek_left : returns the left-peek element of the dequeue (the first). O(1)
    show_dequeue : show all data of the dequeue. O(n)

Types supported : all python data types
 """


# IMPLEMENTATION OF DEQUEUE

import collections


def create_void():
    """
    :return: empty dequeue
    """
    return collections.deque([])


def is_void(dq):
        """
        :param dq: dequeue
        :return: boolean
        """
        return not dq


def push_right(dq, e):
    """
    :param dq: dequeue
    :param e: element
    :return: void
    """
    dq.append(e)


def push_left(dq, e):
    """
    :param dq: dequeue
    :param e: element
    :return: void
    """
    dq.appendleft(e)


def pop(dq):
    """
    :param dq: dequeue
    :return: void
    """
    dq.pop()


def pop_left(dq):
    """
    :param dq: dequeue
    :return: void
    """
    dq.popleft()


def peek_right(dq):
    """
    :param dq: dequeue
    :return: right-peek element of the dequeue
    """
    return dq[-1]


def peek_left(dq):
    """
    :param dq: dequeue
    :return: left-peek element of the dequeue
    """
    return dq[0]


def show_dequeue(dq):
    """
    :param dq: dequeue
    :return: void
    """
    for i in dq:
        print(i)
