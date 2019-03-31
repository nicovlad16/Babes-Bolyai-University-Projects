import sys

from domain.graph import ValidException


def accessible(graph, vertex):
    """Returns the set of vertices of the graph that are accessible
    from the given vertex."""
    accesible = set()
    accesible.add(vertex)
    lst = [vertex]
    while len(lst) > 0:
        x = lst[0]
        lst = lst[1:]
        for y in graph.parseNout(x):
            if y not in accesible:
                accesible.add(y)
                lst.append(y)
    return accesible


def dfs_get_strongly_connected_components(graph):
    """Returns a list of the strongly connected components of a graph."""
    #  or it should -_-
    visited = []
    scc = []
    for node in graph.parseX():
        if node not in visited:
            DFS_algo = accessible(graph, node)
            scc.append(DFS_algo)
            # print(DFS_algo)
            # for i in DFS_algo:
            #     if i not in visited:
            #         visited.append(i)
            visited = DFS_algo
    return scc


def bellman_ford(graph, s, t):
    if not graph.isVertex(s) or not graph.isVertex(t):
        raise ValidException("Inexisting vertices.")

    dist = {}
    prev = {}
    for i in graph.parseX():
        dist[i] = sys.maxsize
        prev[i] = None
    dist[s] = 0
    changed = True
    k = 0
    vertices = graph.get_number_of_vertices()

    while changed and k < vertices:
        changed = False
        for x in graph.parseX():
            for y in graph.parseNout(x):
                if dist[y] > dist[x] + graph.get_cost(x, y):
                    dist[y] = dist[x] + graph.get_cost(x, y)
                    prev[y] = x
                    changed = True
        k += 1

    for x in graph.parseX():
        for y in graph.parseNout(x):
            if dist[y] > dist[x] + graph.get_cost(x, y):
                raise ValidException("Negative cycle.")
    return dist, prev


def find(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]


def union(parent, rank, vertex1, vertex2):
    root1 = find(parent, vertex1)
    root2 = find(parent, vertex2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def minimal_spanning_tree_kruskal(graph):
    """Create a minimal spanning tree from an existing graph.
    Returns: a list with the edges and their costs. """
    parent = {}
    rank = {}
    minimum_spanning_tree = set()
    for vertex in graph.parseX():
        parent[vertex] = vertex
        rank[vertex] = 0

    edges = []
    for x in graph.parseX():
        for y in graph.parseNout(x):
            edge = (graph.get_cost(x, y), x, y)
            edges.append(edge)

    edges.sort(key=lambda x: x[0])

    no_of_vertices = graph.get_number_of_vertices()
    for edge in edges:
        cost, vertex1, vertex2 = edge
        if find(parent, vertex1) != find(parent, vertex2):
            union(parent, rank, vertex1, vertex2)
            minimum_spanning_tree.add(edge)
            if len(minimum_spanning_tree) == no_of_vertices - 1:
                break

    return minimum_spanning_tree


#
# def valid_cover(graph, cover):
#     valid = True
#     num_edge = {}
#     for x in graph.parseX():
#         num_edge[x] = 0
#
#     for x in graph.parseX():
#         for y in graph.parseNout(x):
#             if x not in cover and y not in cover:
#                 valid = False
#                 num_edge[x] += 1
#                 num_edge[y] += 1
#
#     return valid, num_edge
#
#
# def vertex_cover(graph):
#     cover = []
#     valid, num_edge = valid_cover(graph, cover)
#
#     while not valid:
#         m = [x for x in num_edge.keys() if num_edge[x] == max(num_edge.values())][0]
#         cover.append(m)
#         valid, num_edge = valid_cover(graph, cover)
#
#     return cover

def get_max_vertex_degree(graph):
    max_vertex = 0
    max_degree = 0
    for x in graph.parseX():
        if graph.get_outDegreeX(x) > max_degree:
            max_degree = graph.get_outDegreeX(x)
            max_vertex = x
    return max_vertex, max_degree


def vertex_cover(graph):
    cover = []
    edges = []

    for x in graph.parseX():
        for y in graph.parseNout(x):
            edges.append((x, y))
            edges.append((y, x))

    while len(edges):
        max_vertex, max_degree = get_max_vertex_degree(graph)
        if max_degree == 0:
            break
        for i in graph.parseNout(max_vertex):
            edges.remove((max_vertex, i))
            edges.remove((i, max_vertex))
        graph.remove_vertex(max_vertex)
        cover.append(max_vertex)

    return cover

# def vertex_cover(graph):
#     while graph.get_number_of_edges() > 0:
#         cover = []
#         for x in graph.parseX():
#             break
#         for y in graph.parseNout(x):
#             break
#         graph.remove_vertex(x)
#         graph.remove_vertex(y)
#         cover.append(x)
#         cover.append(y)
#     return cover
