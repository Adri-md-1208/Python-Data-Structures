"""
Python-Data-Structures by Adrian Morales Dato
GitHub : Adri-md-1208
E-mail : a.morales.2019@alumnos.urjc.es
Released under a "GPLv3" license


Data structure : graph (digraph)

Description:
    A graph is a data structure that represents a collection of vertices
    connected by edges. This data structure can be performed as a python
    dictionary with sets as values, representing the edges, and keys (arrays)
    representing the vertices. The graph is optionaly weighed.

Operations and asymptotic complexity (class Vertex):
    __init__: create an empty vertex. O(1)
    add_neighbour: adds a neighbour to the adjacents set. O(1)
    remove_neighbour: remove a neighbour from the adjacents set. O(1)
    get_adjacents: returns the set of adjacent vertices. O(1)
    __repr__: prints the vertex info. O(1)
    __str__: prints the vertex data. O(1)

Operations and asymptotic complexity (class Graph):
    create_void : creates an empty dictionary (empty graph).O(1)
    is_empty : returns true if the graph is empty. O(1)
    insert_vertex : inserts a vertex with an empty adjacency list. O(1)
    insert_edge : inserts an edge between two vertices. O(n)
    show_graph : prints all vertices and his neighbours. O(n)

Types supported : all python data types
"""


# IMPLEMENTATION OF GRAPH

class Vertex:

    def __init__(self, data):
        """
        Constructor of the vertex
        :param data: data of the vertex
        :return: None
        """
        self.data = data
        self.adjacents = {}

    def add_neighbour(self, vertex, weight=0):
        """
        Appends a vertex in the adjacents array
        :param vertex: a vertex neighbour
        :param weight: optional weight of the edge
        :return: None
        """
        self.adjacents[vertex] = weight

    def remove_neighbour(self, vertex):
        """
        Removes a vertex of the adjacents array
        :return: the vertex removed
        """
        self.adjacents.remove(vertex)

    def get_adjacents(self):
        """
        Returns the list of neighbours
        :return: list of neighbours
        """
        return self.adjacents

    def __repr__(self):
        """
        Represent the Graph class in text format
        :return: data and adjacents vertices
        """
        return f"< Vertex (data={self.data}, adjacent={self.adjacents}) >"

    def __str__(self):
        """
        Reprents the Vertex as a string
        :return: the string representation of the Vertex
        """
        return str(self.data)


class Graph:

    def __init__(self, vertices=None):
        """
        Constructor for the graph
        :param d: set of vertices
        :return: None
        """
        if vertices is None:
            vertices = set()
        self.vertices = vertices

    def is_empty(self):
        """
        :return: boolean
        """
        return self.vertices

    def insert_vertex(self, vert):
        """
        :param vert: vertex
        :return: void
        """
        self.vertices.add(vert)

    def insert_edge(self, vert1, vert2):
        """
        :param vert1: first vertex
        :param vert2: second vertex
        :return: void
        """
        if vert1 in self.vertices:
            vert1.add_neighbour(vert2)
        else:
            self.vertices.add(vert1)
            self.vertices[vert1]

    def show_graph(self):
        """
        :return: void
        """
        for v in self.vertices:
            print(v, '->', end='')
            for e in v.get_adjacents():
                print(' ', e, end='')
            print()
