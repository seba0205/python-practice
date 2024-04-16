
# This set class was taken from python-disjoint-set by imressed on GitHub
# implements a disjoint set data structure with functions find and union
class Set:
    """A implementation for a disjoint-set data structure."""
    _disjoint_set = list()

    def __init__(self, init_arr):
        self._disjoint_set = []
        if init_arr:
            for item in list(set(init_arr)):
                self._disjoint_set.append([item])

    def _find_index(self, elem):
        for item in self._disjoint_set:
            if elem in item:
                return self._disjoint_set.index(item)
        return None

    def find(self, elem):
        for item in self._disjoint_set:
            if elem in item:
                return self._disjoint_set[self._disjoint_set.index(item)]
        return None

    def union(self, elem1, elem2):
        index_elem1 = self._find_index(elem1)
        index_elem2 = self._find_index(elem2)
        if index_elem1 != index_elem2 and index_elem1 is not None and index_elem2 is not None:
            self._disjoint_set[index_elem2] = self._disjoint_set[index_elem2] + self._disjoint_set[index_elem1]
            del self._disjoint_set[index_elem1]
        return self._disjoint_set

    def get(self):
        return self._disjoint_set


def kruskal(graph_map):
    """Kruskal's algorithm to find a MST'"""
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
    disjoint_set = Set(vertices)

    while i < len(edges) - 1:
        edge = edges[i]
        start_node = edge.get_from_node()
        end_node = edge.get_to_node()
        i += 1
        if disjoint_set.find(start_node) != disjoint_set.find(end_node):
            tree.add(edge)
            disjoint_set.union(start_node, end_node)

    for edge in tree:
        print(str(edge))
    return tree


