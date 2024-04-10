from kruskal import kruskal
from dijkstra import dijkstra
from graph import make_random_graph

'''
Use make_random_graph to generate a random graph. 
Takes in the total number of vertices and whether or not the graph is directed
'''
graph_dijkstra_test = make_random_graph(8, False)

graph_dijkstra_test.print()

dijkstra(graph_dijkstra_test, graph_dijkstra_test.get_vertex(0), graph_dijkstra_test.get_vertex(3))

