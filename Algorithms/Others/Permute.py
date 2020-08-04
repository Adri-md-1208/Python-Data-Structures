"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Algorithm : permute

Description:
    Permute algorithm use backtracking for search all posible combinations of given data.

Algorithmic efficiency : O(log n)
"""


# PERMUTE

def permute(length, list):
    """
    :param length: number of permutations
    :param list: list with elements to permute
    """
    if length == 1:
        return list
    else:
        return [ x + y
                for x in permute(1, list)
                for y in permute(length-1, list)
                ]


lista = ['a', 'b', 'c']
print(permute(3, lista))
print(permute(2, lista))
print(permute(1, lista))
