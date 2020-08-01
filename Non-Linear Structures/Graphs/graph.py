"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : graph (digraph)

Description:
    A graph is a data structure that represents a collection of nodes (vertices) connected by edges.
    This data structure can be performed as a python dictionary with sets as values, representing the
    edges, and keys representing the vertices.
Operations and asymptotic complexity: create_void : returns an empty node. O(1)
    create_void : creates an empty dictionary (empty graph).O(1)
    is_void : returns true if the graph is empty. O(1)
    insert_vertex : inserts a vertex with an empty adjacency list. O(1)
    insert_edge : inserts an edge between two vertices. O(n²)
    show_vertices : prints all vertices. O(n)
    show_edges : prints all edges. O(n²)

Types supported : all python data types
"""


# IMPLEMENTATION OF GRAPH

def create_void():
    """
    :return: empty graph
    """
    return Graph


class Graph:
    def __init__(self, gdict=None):
        """
        Constructor for the graph
        :param d: dictionary of the graph
        """
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def is_void(self):
        """
        :return: boolean
        """
        return self.gdict is None

    def insert_vertex(self, vert):
        """
        :param vert: vertex
        :return: void
        """
        if vert not in self.gdict:
            self.gdict[vert] = []

    def insert_edge(self, edge):
        """
        :param edge: pair of vertices
        :return: void
        """
        vert1, vert2 = edge
        if vert1 in self.gdict:
            self.gdict[vert1].append(vert2)
        else:
            self.insert_vertex(vert1)
            self.insert_edge([vert1, vert2])

    def show_vertices(self):
        """
        :return: void
        """
        for v in self.gdict:
            print(v)

    def show_edges(self):
        """
        :return: void
        """
        for v in self.gdict:
            print(v, ':')
            for e in v:
                print(v)
