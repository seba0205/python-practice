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
        valstr = str(self.val) + " -> "
        for n in self.neighbours:
            valstr = valstr + str(n.to_node.val) + ","
        return valstr


class Edge:
    def __init__(self, from_node, to_node, weight=0):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

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
        self.vertices.append(Vertex(val))

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
    def print(self):
        for e in self.edges:
            print(str(e.from_node.val) + " -> " + str(e.to_node.val) + " | weight = " + str(e.weight))
        for v in self.vertices:
            print(str(v))


def dijkstra(graph, start, goal):
    distances = {}
    distances[start] = 0
    for v in graph.vertices:
        distances[v] = 1000


graph = Graph(False)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_edge(1, 4, 2)
graph.add_edge(2, 3, 1)
graph.add_edge(3, 1, 4)
graph.add_edge(4, 5, 2)
