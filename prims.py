import random

import graph


def prims(graph):
    visited = set()
    unvisited = set()
    mst = set()
    mst_vertices = set()

    for vertex in graph.get_vertices():
        unvisited.add(vertex)

    starting_vertex = graph.get_vertex((random.randint(0, len(graph.get_vertices())-1)))
    print(len(mst))
    edges = list(starting_vertex.get_neighbours())
    while len(mst_vertices) < len(unvisited):
        min_edge = get_min(edges)
        mst.add(min_edge)
        mst_vertices.add(min_edge.get_to_node())
        edges.remove(min_edge)
        for i in range(len(min_edge.get_to_node().get_neighbours())):
            edge = min_edge.get_to_node().get_neighbours()[i]
            if edge not in mst:
                edges.append(edge)

    for edge in mst:
        print(str(edge))



def get_min(edges):
    min_num = 100
    min_edge = None
    for i in range(len(edges)):
        edge = edges[i]
        if edge.get_weight() < min_num:
            min_num = edge.get_weight()
            min_edge = edge
    return min_edge





