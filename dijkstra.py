
def dijkstra(graph_map, start, end):
    """Implementation of Dijkstra's algorithm"""
    # collection of unvisited nodes
    unvisited = set()
    # dictionary of distances for each node. start is initialised to 0
    distance = {start: 0}
    # for each vertex in the graph, initialise distance to very high for all unvisited nodes
    for vertex in graph_map.get_vertices():
        if vertex != start:
            distance[vertex] = 1000
            unvisited.add(vertex)

    # Getting the node with the current minimum distance to it in the unvisited set
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
        # for each of the neighbours of the current node,
        # check if their distance is shorter than the distance to the current node + the wight
        # if so, update the shortest distance
        for v in current_vertex.get_neighbours():
            alt = distance[current_vertex] + v.get_weight()
            if alt < distance[v.get_to_node()]:
                distance[v.get_to_node()] = alt

    # prints out every node with the distance from start
    for i in distance:
        print(str(i) + " - Distance from start:" + str(distance[i]))
    print("---")

    path = {end: distance[end]}
    # finding the shortest path back from end goal
    current = end
    # while the current node is not the start node, get the neighbour with the minimum distance
    # continue until a path back to the start node has been found
    while current != start:
        min_value = 1000
        min_vertex = None
        for v in current.get_neighbours():
            if distance[v.get_to_node()] < min_value:
                min_value = distance[v.get_to_node()]
                min_vertex = v.get_to_node()
            current = min_vertex
        path[current] = distance[current]

    # nicely prints out the path back
    print("Shortest distance from " + str(start) + " to " + str(end) + " is " + str(distance[end]))
    while path != {}:
        item = path.popitem()
        print(str(item[0]) + " -  Current distance from start: " + str(item[1]))

