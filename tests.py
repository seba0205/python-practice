from kruskal import kruskal
from dijkstra import dijkstra
from graph import Graph, make_graph_from_matrix, Vertex

graph_directed_one = make_graph_from_matrix(
    [[0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1],
     [0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0]])

graph_directed_two = make_graph_from_matrix(
    [[0, 5, 0, 0, 0, 0], [0, 0, 0, 3, 0, 0], [1, 4, 0, 0, 5, 0], [0, 0, 0, 0, 0, 6],
     [0, 3, 0, 1, 0, 4], [0, 0, 0, 0, 0, 0]])

graph_dijkstra_test = make_graph_from_matrix([[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]])

dijkstra(graph_dijkstra_test, graph_dijkstra_test.get_vertex(0), graph_dijkstra_test.get_vertex(3))

kruskal(graph_directed_one)
print("--")
kruskal(graph_directed_two)
