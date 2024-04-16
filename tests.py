from kruskal import kruskal
from dijkstra import dijkstra
from prims import prims
from graph import make_random_graph

'''
Use make_random_graph to generate a random graph. 
Takes in the total number of vertices and whether or not the graph is directed
'''
graph_dijkstra_test = make_random_graph(8, False)


prims(graph_dijkstra_test)
print("compare")
kruskal(graph_dijkstra_test)


