"""
Utility for printing the graph in pseudo graphical mode
"""


class graphPlot:

    def __init__(self):
        pass

    def print_vertices(self, vertices):
        horizontal = ' ~~~ '
        vertical = '|'
        for i in range(len(vertices)-1):
            print(horizontal, end='')
            if i == len(vertices)-2:
                print(horizontal)
        i = 0
        for vertex in vertices:
            print(vertical, vertex, vertical, end='')
            if i == len(vertices)-1:
                print()
            i += 1
        for i in range(len(vertices)-1):
            print(horizontal, end='')
            if i == len(vertices)-2:
                print(horizontal)


vertices = set()
for i in ['A', 'B', 'C', 'D']:
    vertices.add(i)
g = graphPlot()
g.print_vertices(vertices)
