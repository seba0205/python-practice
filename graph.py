import random
import numpy as np


class Vertex:
    """A vertex in a graph"""

    def __init__(self, val):
        self.val = val
        self.neighbours = []

    def add(self, other):
        if other not in self.neighbours:
            self.neighbours.append(other)

    def get_neighbours(self):
        return self.neighbours

    def __str__(self):
        return str(self.val)


class Edge:
    """An edge between two vertices."""

    def __init__(self, from_node, to_node, weight=0, flow=False):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight   # Capacity for a flow network
        self.flow = 0 if flow else None

    def compare(self, other):
        return self.weight < other.weight

    def get_flow(self):
        return self.flow

    def get_weight(self):
        return self.weight

    def get_from_node(self):
        return self.from_node

    def get_to_node(self):
        return self.to_node

    def __str__(self):
        return f"({self.from_node}) --  {self.weight} -- ({self.to_node})"


class Graph:
    """A graph of vertices and edges"""
    def __init__(self, directed, flow=False):
        self.vertices = []
        self.edges = []
        self.directed = directed
        self.flow = flow

    def add_vertex(self, val):
        if val not in self.vertices:
            self.vertices.append(val)

    def add_edge(self, from_val, to_val, weight,flow):
        from_node = next(n for n in self.vertices if n.val == from_val)
        to_node = next(n for n in self.vertices if n.val == to_val)

        edge = Edge(from_node, to_node, weight,flow)
        self.edges.append(edge)
        from_node.neighbours.append(edge)

        if not self.directed:
            edge = Edge(to_node, from_node, weight)
            to_node.neighbours.append(edge)
            self.edges.append(edge)

    def get_vertices(self):
        return self.vertices

    def get_vertex(self, vertex):
        return self.vertices[vertex]

    def get_edges(self):
        return self.edges

    def print(self):
        for e in self.edges:
            print(str(e.from_node.val) + " -> " + str(e.to_node.val) + " | weight = " + str(e.weight))


def make_graph_from_matrix(matrix,flow=False):
    """Given a matrix, creates a graph object"""
    graph = Graph(True)
    for i in range(len(matrix)):
        graph.add_vertex(Vertex(i + 1))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0:
                graph.add_edge(row + 1, col + 1, matrix[row][col],flow)
    return graph


def make_random_graph(vertex_num, directed=False, flow=False):
    """Generates a random graph with a given number of vertices"""
    matrix = np.zeros((vertex_num, vertex_num))
    for i in range(vertex_num):
        for j in range(vertex_num):
            if directed:
                matrix[i][j] = random.randint(0, 9)
                matrix[j][i] = matrix[i][j]
            else:
                matrix[i][j] = random.randint(0, 9)
    return make_graph_from_matrix(matrix,flow)

