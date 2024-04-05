from graph import Vertex, Edge, Graph


def dijkstra(graph_map, start,end):
    unvisited = set()
    distance = {start: 0}
    for vertex in graph_map.get_vertices():
        if vertex != start:
            distance[vertex] = 1000
            unvisited.add(vertex)
    current_vertex = start
    while len(unvisited) > 0:
        unvisited.discard(current_vertex)
        min_value = 1000
        min_vertex = start
        for v in unvisited:
            if distance[v] < min_value:
                min_value = distance[v]
                min_vertex = v
        current_vertex = min_vertex
        for v in current_vertex.get_neighbours():
            alt = distance[current_vertex] + v.get_weight()
            if alt < distance[v.get_to_node()]:
                distance[v.get_to_node()] = alt

    return distance

