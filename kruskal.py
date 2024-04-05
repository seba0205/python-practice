from graph import Vertex, Edge, Graph


# Implementation of kruskal's algorithm to find a minimum spanning tree
def kruskal(graph_map):
    tree = set()
    vertices = graph_map.get_vertices()
    edges = graph_map.get_edges()
    i = 0
    parent = []
    rank = []

    # helper function to sort the edges by minimum weight
    def sort_edges(e):
        return e.weight

    edges.sort(key=sort_edges)

    while i < len(edges) - 1:
        edge = edges[i]
        start_node = edge.get_from_node()
        end_node = edge.get_to_node()


graph1 = Graph(False)
graph1.add_vertex(1)
graph1.add_vertex(2)
graph1.add_vertex(3)
graph1.add_vertex(4)
graph1.add_vertex(5)
graph1.add_edge(1, 4, 2)
graph1.add_edge(2, 3, 1)
graph1.add_edge(3, 1, 4)

kruskal(graph1)
