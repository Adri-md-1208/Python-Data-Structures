"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.u3rjc.es
Released under a "GPLv3" license


Data structure : stack

Description:
    The stack data structure is based on the python list, but with the particularity that the last
    element you input is the first to go out (LIFO).

Operations and asymptotic complexity:
    create_void : create an empty stack. O(1)
    is_void : return true if the sll have no elements. O(1)
    push : insert a element in the tail (our peek). O(1)
    pop : removes the last element of the stack. O(n)
    peek : returns the peek element of the stack (the last). O(1)
    show_stack : show all data of the stack. O(n)

Types supported : all python data types
 """


# IMPLEMENTATION OF STACK

def create_void():
    """
    :return: empty stack
    """
    return Stack


class Stack:
    def __init__(self):
        self.stack = []

    def is_void(self):
        """
        :return: boolean
        """
        return self.stack == []

    def push(self, data):
        """
        :param data: element to insert
        :return: void
        """
        self.stack.append(data)

    def pop(self):
        """
        :return: void
        """
        if not self.is_void():
            self.stack.pop()

    def peek(self):
        """
        :return: the last element of the stack
        """
        return self.stack[-1]

    def show_stack(self):
        """
        :return: void
        """
        for i in self.stack:
            print(i)
