'''
Data structure : array
Description:
    An array is a static data structure that contains a finite number of elements that are all of the
    same type. The array type is predefined by Python and we do not have to implement it.
Operations:
    insert : add an element at the index position. O(1)
    delete : remove an element at the index position. O(1)
    search : search an element and return his index. O(n)
    show_array : show all the elements of the array. O(n)
    update : change the value of the element at the index position. O(1)
Complexity:
    O(1) : insert, delete, update
    O(n) : search, show_array
Types supported (more commons):
    b : signed integer of 1 byte
    B : unsigned integer of 1 byte
    i : signed integer of 2 bytes
    I : unsigned integer of 2 bytes
    f : float of 4 bytes
    d : double of 8 bytes
'''

from array import *

# IMPLEMENTATION OF ARRAY

def create_void(t):
    '''
    :param t: type of the elements
    :return: void array
    '''
    return array(t, [])

def insert_element(a, i, e):
    a.insert(i, e)

# show_array
def show_array(a):
    for i in a:
        print(i)

# Testing the implementation

typeArray = "b"
i, ii, iii = 0, 1, 2
a, b, c = 1, 2, 3

insert_element(myArray, i, a)
insert_element(myArray, ii, b)
insert_element(myArray, iii, c)
show_array(myArray)

