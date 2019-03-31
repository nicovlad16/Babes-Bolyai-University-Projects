from time import time

from domain.algorithms import dfs_get_strongly_connected_components, bellman_ford, minimal_spanning_tree_kruskal, \
    vertex_cover
from domain.graph import Graph, ValidException
from repo.repository import Repository


class CtrlException(Exception):
    pass


class Controller():
    def __init__(self, repo):
        self.__time_of_last_operation = time() - time()
        self.__repo = repo
        self.__graph = self.__repo.get_current_element()


    def get_time(self):
        return self.__time_of_last_operation


    def save_file(self, filename):
        """
        Saves the current graph to a file.
        """
        time_in = time()
        self.__repo.add(self.__graph)
        self.__repo.write_to_file(filename)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in


    def load_file(self, filename):
        """
        Gets the current graph from the file, and that file will be the current repo.
        The graph is directed.
        """
        time_in = time()
        self.__repo = Repository(filename, "big_graph")
        self.__graph = self.__repo.get_current_element()
        time_out = time()
        self.__time_of_last_operation = time_out - time_in


    def load_modified_graph(self, filename):
        """
        Gets the current graph from the file, and that file will be the current repo.
        The graph is directed.
        """
        time_in = time()
        self.__repo = Repository(filename, "modified")
        self.__graph = self.__repo.get_current_element()
        time_out = time()
        self.__time_of_last_operation = time_out - time_in


    def load_undirected_graph(self, filename):
        """
        Gets the current graph from the file, and that file will be the current repo.
        The graph is undirected.
        """
        time_in = time()
        self.__repo = Repository(filename, "undirected")
        self.__graph = self.__repo.get_current_element()
        time_out = time()
        self.__time_of_last_operation = time_out - time_in


    def add_vertex(self, x):
        """Adds a vertex to the graph."""
        time_in = time()
        self.__graph.addVertex(x)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in


    def add_edge(self, x, y):
        """Adds an edge to the graph."""
        time_in = time()
        self.__graph.addEdge(x, y)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in


    def add_cost(self, x, y, cost):
        """Adds a cost to an existing edge."""
        time_in = time()
        self.__graph.addCost(x, y, cost)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in


    def number_of_vertices(self):
        """Get the number of vertices in the graph."""
        time_in = time()
        number = self.__graph.get_number_of_vertices()
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        return number


    def number_of_edges(self):
        """Get the number of edges in the graph."""
        time_in = time()
        number = self.__graph.get_number_of_edges()
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        return number


    def out_degree(self, x):
        """Get the out degree of a given vertex."""
        time_in = time()
        number = self.__graph.get_outDegreeX(x)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        return number


    def in_degree(self, x):
        """Get the in degree of a given vertex."""
        time_in = time()
        number = self.__graph.get_inDegreeX(x)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        return number


    def is_edge(self, x, y):
        """Returns true if there is an edge between the vertices x and y, false otherwise."""
        time_in = time()
        ok = self.__graph.isEdge(x, y)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        return ok


    def is_vertex(self, x):
        """Returns true if the vertex x exists, false otherwise."""
        time_in = time()
        ok = self.__graph.isVertex(x)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        return ok


    def update_cost(self, x, y, cost):
        """Update the cost of an edge."""
        time_in = time()
        self.__graph.update_cost(x, y, cost)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in


    def get_vertices(self):
        """Return a string containing all the vertices in the graph."""
        time_in = time()
        s = ""
        c = 0
        for i in self.__graph.parseX():
            s += str(i) + "  "
            c += 1
            if c % 20 == 0:
                s += "\n"
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        return s


    def get_all_edges(self):
        """Return a string containing all the edges in the graph."""
        time_in = time()
        s = ""
        c = 0
        for i in self.__graph.parseX():
            for j in self.__graph.parseNout(i):
                s += "(" + str(i) + ", " + str(j) + ")   "
                c += 1
                if c % 10 == 0:
                    s += "\n"
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        return s


    def get_in_edges_of_vertex(self, x):
        """Return a string containing all the edges in the graph, having as end point the given vertex."""
        time_in = time()
        s = ""
        c = 0
        for i in self.__graph.parseNin(x):
            s += str(i) + "  "
            c += 1
            if c % 20 == 0:
                s += "\n"
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        return s


    def get_out_edges_of_vertex(self, x):
        """Return a string containing all the edges in the graph, having as start point the given vertex."""
        time_in = time()
        s = ""
        c = 0
        for i in self.__graph.parseNout(x):
            s += str(i) + "  "
            c += 1
            if c % 20 == 0:
                s += "\n"
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        return s


    def print_graph(self):
        """Return a string containing all the vertices, with their in and out edges."""
        time_in = time()
        s = str(self.__graph)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        return s


    def remove_vertex(self, x):
        """Removes a vertex from the graph."""
        time_in = time()
        self.__graph.remove_vertex(x)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in


    def remove_edge(self, x, y):
        """Removes an edge from the graph."""
        time_in = time()
        self.__graph.remove_edge(x, y)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in


    def remove_cost(self, x, y):
        """Removes the cost of an edge from the graph."""
        time_in = time()
        self.__graph.remove_cost(x, y)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in


    def get_cost(self, x, y):
        """Returns the cost of an edge from the graph."""
        time_in = time()
        cost = self.__graph.get_cost(x, y)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        return cost


    def get_strongly_connected_components_by_dfs(self):
        """it should save each connencted component as a new graph;
        but it doesn't even work properly -_- """
        time_in = time()
        for i in dfs_get_strongly_connected_components(self.__graph):
            print(i)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in


    def find_lowest_cost_walk(self, x, y):
        """ Write a program that, given a graph with costs and
        two vertices, finds a lowest cost walk between the
        given vertices, or prints a message if there are
        negative cost cycles accessible from the starting
        vertex. The program will use a matrix defined as
        d[x,k]=the cost of the lowest cost walk from s to x
        and of length at most k, where s is the starting vertex. """
        time_in = time()
        dist, prev = bellman_ford(self.__graph, x, y)
        cost = 0
        walk = []
        end = y
        while y != None:
            walk.append(y)
            cost += dist[y]
            y = prev[y]
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        if len(walk) < 2:
            raise ValidException("The walk doesn't exist.")
        return dist[end], walk[::-1]


    def minimal_spanning_tree_kruskal(self, filename):
        """Finds a minimal spanning tree of the current
         graph using kruskal's algorithm.
         The resulting graph is saved to a file."""
        time_in = time()
        edges = minimal_spanning_tree_kruskal(self.__graph)
        new_graph = Graph()
        for edge in edges:
            x = edge[1]
            y = edge[2]
            try:
                new_graph.addVertex(x)
            except ValidException:
                pass
            try:
                new_graph.addVertex(y)
            except ValidException:
                pass
            new_graph.addEdge(x, y)
            cost = edge[0]
            new_graph.addCost(x, y, cost)

        self.__graph = new_graph
        self.save_file(filename)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in


    def find_vertex_cover(self):
        time_in = time()
        cover = vertex_cover(self.__graph)
        time_out = time()
        self.__time_of_last_operation = time_out - time_in
        return cover
