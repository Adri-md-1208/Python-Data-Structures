"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Algorithm : breadth fisrt search (BFS)

Description:
    The BFS algorithm traverses a graph breadth ward motion and uses a queue for the searched nodes.

Algorithmic efficiency : O(n)
"""


# DEPTH FIRST SEARCH

class Graph:
    def __init__(self, gdict=None):
        """
        Constructor for the graph
        :param d: dictionary of the graph
        """
        if gdict is None:
            gdict = {}
        self.gdict = gdict

def bfs(graph, start, visited=None):
    """
    :param start: first node where we start searching
    :param visited: visited nodes
    :return: list with the traverse
    """
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

