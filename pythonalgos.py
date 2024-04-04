class Vertex:
    def __init__(self, val):
        self.val = val
        self.neighbours = []

    def add(self, other):
        if other not in self.neighbours:
            self.neighbours.append(other)

    def __str__(self):
        valstr = str(self.val) + " -> "
        for n in self.neighbours:
            valstr = valstr + str(n.val) + ","
        return valstr


class Edge:
    def __init__(self, from_node, to_node, weight=0):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __str__(self):
        return f"({self.from_node}) --  {self.weight} -- ({self.to_node})"


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, val):
        self.vertices.append(Vertex(val))

    def add_edge(self, from_val, to_val, weight):
        from_node = next(n for n in self.vertices if n.val == from_val)
        to_node = next(n for n in self.vertices if n.val == to_val)
        self.edges.append(Edge(from_node, to_node, weight))
        from_node.neighbours.append(to_node)
        to_node.neighbours.append(from_node)

    def print(self):
        for e in self.edges:
            print(str(e.from_node.val) + " -> " + str(e.to_node.val) + " | weight = " + str(e.weight))
        for v in self.vertices:
            print(str(v))


graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_edge(1, 4, 2)
graph.add_edge(2, 3, 1)
graph.add_edge(3, 1, 4)
graph.add_edge(4, 5, 2)

graph.print()
