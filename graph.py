class Vertex:
    def __init__(self, val):
        self.val = val
        self.neighbours = []
        self.visited = False

    def add(self, other):
        if other not in self.neighbours:
            self.neighbours.append(other)

    def get_neighbours(self):
        return self.neighbours

    def __str__(self):
        return str(self.val)


class Edge:
    def __init__(self, from_node, to_node, weight=0):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def compare(self, other):
        return self.weight < other.weight

    def get_weight(self):
        return self.weight

    def get_from_node(self):
        return self.from_node

    def get_to_node(self):
        return self.to_node

    def __str__(self):
        return f"({self.from_node}) --  {self.weight} -- ({self.to_node})"


class Graph:
    def __init__(self, directed):
        self.vertices = []
        self.edges = []
        self.directed = directed

    def add_vertex(self, val):
        if val not in self.vertices:
            self.vertices.append(val)

    def add_edge(self, from_val, to_val, weight):
        from_node = next(n for n in self.vertices if n.val == from_val)
        to_node = next(n for n in self.vertices if n.val == to_val)

        edge = Edge(from_node, to_node, weight)
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


def make_graph_from_matrix(matrix):
    # note: when creating a graph from a matrix, it doesn't matter what the directed boolean
    # if the matrix is symmetrical, it will be undirected
    # so, we can just set it to true automatically
    graph = Graph(True)
    for i in range(len(matrix)):
        graph.add_vertex(Vertex(i+1))
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] != 0:
                graph.add_edge(row + 1, col + 1, matrix[row][col])
    return graph


graph = Graph(False)
graph.add_vertex(Vertex(1))
graph.add_vertex(Vertex(2))
graph.add_vertex(Vertex(3))
graph.add_vertex(Vertex(4))
graph.add_vertex(Vertex(5))
graph.add_edge(1, 4, 2)
graph.add_edge(2, 3, 1)
graph.add_edge(3, 1, 4)
graph.add_edge(4, 5, 2)
