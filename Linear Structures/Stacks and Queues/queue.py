"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : queue

Description:
    The queue data structure is based on the python list, but with the particularity that the first
    element you input is the first to go out (FIFO).

Operations and asymptotic complexity:
    create_void : create an empty queue. O(1)
    is_void : return true if the queue have no elements. O(1)
    push : insert a element in the header. O(1)
    pop : removes the last element of the queue. O(n)
    peek : returns the peek element of the queue (the last). O(n)
    show_queue : show all data of the queue. O(n)

Types supported : all python data types
 """


# IMPLEMENTATION OF QUEUE

def create_void():
    """
    :return: empty queue
    """
    return Queue


class Queue:
    def __init__(self):
        self.queue = []

    def is_void(self):
        """
        :return: boolean
        """
        return self.queue == []

    def push(self, data):
        """
        :param data: element to insert
        :return: void
        """
        if data not in self.queue:
            self.queue.insert(0, data)

    def pop(self):
        """
        :return: void
        """
        if not self.is_void():
            self.queue.pop()

    def peek(self):
        """
        :return: the last element of the queue
        """
        return self.queue[-1]

    def show_queue(self):
        """
        :return: void
        """
        for i in self.queue:
            print(i)
