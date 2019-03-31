import random


class ValidException(Exception):
    pass


class Graph():
    """A directed graph, represented as two maps,
    one from each vertex to the set of outbound neighbours,
    the other from each vertex to the set of inbound neighbours."""


    def __init__(self, n=0):
        """Creates a graph with n vertices (numbered from 0 to n-1)
        and no edges."""
        self.__number_of_vertices = n
        self.__number_of_edges = 0
        self.__outbound_neighbours = {}
        self.__inbound_neighbours = {}
        self.__cost = {}
        for i in range(n):
            self.__outbound_neighbours[i] = []
            self.__inbound_neighbours[i] = []


    def get_number_of_vertices(self):
        return self.__number_of_vertices


    def get_number_of_edges(self):
        return self.__number_of_edges


    def parseX(self):
        """Returns an iterable containing all the vertices"""
        return self.__outbound_neighbours.keys()


    def parseNout(self, x):
        """Returns an iterable containing the outbound neighbours of x"""
        if not self.isVertex(x):
            raise ValidException("Inexisting vertex.")
        return self.__outbound_neighbours[x]


    def parseNin(self, y):
        """Returns an iterable containing the inbound neighbours of x"""
        if not self.isVertex(y):
            raise ValidException("Inexisting vertex.")
        return self.__inbound_neighbours[y]


    def isEdge(self, x, y):
        """Returns True if there is an edge from x to y, False otherwise"""
        if self.isVertex(x) and self.isVertex(y):
            return y in self.__outbound_neighbours[x]
        else:
            raise ValidException("Invalid vertices.")


    def isVertex(self, x):
        """Return True if the vertex x exists, False otherwise"""
        if x < 0:
            raise ValidException("Invalid vertex.")
        return x in self.__inbound_neighbours.keys()


    def addEdge(self, x, y):
        """Adds an edge from x to y.
        Precondition: there is no edge from x to y"""
        if self.isEdge(x, y):
            raise ValidException("Existing edge.")
        self.__outbound_neighbours[x].append(y)
        self.__inbound_neighbours[y].append(x)
        self.__number_of_edges += 1


    def addVertex(self, x):
        """Adds a new vertex to the graph."""
        if self.isVertex(x):
            raise ValidException("Existing vertex.")
        else:
            self.__outbound_neighbours[x] = []
            self.__inbound_neighbours[x] = []
            self.__number_of_vertices += 1


    def addCost(self, x, y, c):
        """Adds a cost to the existing edge from x to y."""
        if c != 0:
            if not self.isEdge(x, y):
                raise ValidException("Inexisting edge.")
            if (x, y) in self.__cost:
                raise ValidException("Existing cost.")
            self.__cost[(x, y)] = c


    def get_cost(self, x, y):
        """Return the cost of the edge from x to y.
        Precondition: the edge from x to y exists"""
        if self.isEdge(x, y):
            if (x, y) in self.__cost:
                return self.__cost[(x, y)]
            elif self.isEdge(x, y):
                return 0
        else:
            raise ValidException("Inexisting edge.")


    def get_inDegreeX(self, y):
        """Return the in degree of the vertex x, that is how many
        edges have x as end point.
        Precondition: x is a valid vertex"""
        if not self.isVertex(y):
            raise ValidException("Inexisting vertex.")
        return len(self.__inbound_neighbours[y])


    def get_outDegreeX(self, x):
        """Return the out degree of the vertex x, that is how many
        edges have x as starting point.
        Precondition: x is a valid vertex"""
        if not self.isVertex(x):
            raise ValidException("Inexisting vertex.")
        return len(self.__outbound_neighbours[x])


    def update_cost(self, x, y, c):
        """Updates the cost of the edge from x to y.
        Precondition: there is an edge from x to y"""
        if self.isEdge(x, y):
            if c != 0:
                self.__cost[(x, y)] = c
            elif c == 0 and (x, y) in self.__cost:
                del self.__cost[(x, y)]
        else:
            raise ValidException("Inexisting edge.")


    def __str__(self):
        string = ""
        for i in self.parseX():
            string += str(i) + ": in  - " + str(self.parseNin(i)) + "\n"
            for k in range(len(str(i))):
                string += " "
            string += "  out - " + str(self.parseNout(i)) + "\n"
            string += "\n"
        if self.__number_of_vertices == 0:
            string = "The graph is empty."
        return string


    def remove_vertex(self, x):
        """Removes an existing vertex from the graph.
        Precondition: the vertex x exists in the graph"""
        if not self.isVertex(x):
            raise ValidException("Inexisting vertex.")
        else:
            for i in self.parseNin(x):
                self.__outbound_neighbours[i].remove(x)
                self.__number_of_edges -= 1
                if (i, x) in self.__cost:
                    del self.__cost[(i, x)]
            for i in self.parseNout(x):
                self.__inbound_neighbours[i].remove(x)
                self.__number_of_edges -= 1
                if (i, x) in self.__cost:
                    del self.__cost[(i, x)]
            del self.__inbound_neighbours[x]
            del self.__outbound_neighbours[x]
            self.__number_of_vertices -= 1


    def remove_cost(self, x, y):
        """Removes the cost of the edge from x to y.
        Precondition: there is an edge from x to y"""
        if self.isEdge(x, y):
            if (x, y) in self.__cost:
                del self.__cost[(x, y)]
        else:
            raise ValidException("Inexisting edge.")


    def remove_edge(self, x, y):
        """Removes the edge from x to y.
        Precondition: there is an edge from x to y"""
        if not self.isEdge(x, y):
            raise ValidException("Inexisting edge.")
        if (x, y) in self.__cost:
            del self.__cost[(x, y)]
        self.parseNout(x).remove(y)
        self.parseNin(y).remove(x)
        self.__number_of_edges -= 1
