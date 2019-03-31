from domain.graph import Graph, ValidException


class RepoException(Exception):
    pass


class Repository():
    def __init__(self, filename, type_of_file):
        self.__elems = []
        self.__filename = filename
        self.__type_of_file = type_of_file
        try:
            self.__read_from_file()
        except FileNotFoundError:
            raise RepoException("Inexisting file.")


    def __read_from_file(self):
        """
        reads a graph from a file, then adds it to the repository
        """
        if self.__type_of_file == "big_graph":
            self.__load_big_directed_graph()
        elif self.__type_of_file == "modified":
            self.__load_modified_directed_graph()
        elif self.__type_of_file == "undirected":
            self.__load_undirected_graph()


    def add(self, elem):
        """
        :param elem:
        adds an element to the repository
        """
        self.__elems.append(elem)


    def write_to_file(self, filename):
        """
        :param filename:
        creates a new file with given name, having as stored information the last grid added in repo
        """
        graph = self.__elems[-1]
        line = ""
        line += str(graph.get_number_of_vertices())
        line += ";"
        line += str(graph.get_number_of_edges())
        line += "\n"
        for i in graph.parseX():
            for j in graph.parseNout(i):
                if graph.isEdge(i, j):
                    line += str(i) + ';' + str(j)
                    line += ";" + str(graph.get_cost(i, j)) + '\n'
        for i in graph.parseX():
            if graph.get_inDegreeX(i) == 0 and graph.get_outDegreeX(i) == 0:
                line += str(i) + "\n"
        try:
            with open(filename, "r"):
                raise RepoException("There already exists a file with given name.")
        except FileNotFoundError:
            with open(filename, "w")as f:
                f.write(line)


    def get_current_element(self):
        """
        :return: the last element from repo
        """
        return self.__elems[-1]


    def __load_big_directed_graph(self):
        with open(self.__filename, "r") as f:
            line = f.readline().strip()
            if not line:
                raise RepoException("Invalid file.")
            elems = line.split(";")
            if len(elems) != 2:
                raise RepoException("Invalid file.")
            try:
                n = int(elems[0])
                m = int(elems[1])
            except:
                raise RepoException("Invalid file.")

            graph = Graph(n)
            i = 0

            for line in f.readlines():
                line = line.strip()
                if line:
                    a = line.split(";")
                    if len(elems) != 2 and len(elems) != 3:
                        raise RepoException("Invalid file.")
                    try:
                        x = int(a[0])
                        y = int(a[1])
                        graph.addEdge(x, y)
                        try:
                            c = int(a[2])
                            graph.addCost(x, y, c)
                        except:
                            pass
                    except:
                        raise RepoException("Invalid file.")
                    i += 1

            if i != m:
                raise RepoException("Invalid file.")
            self.__elems.clear()
            self.add(graph)


    def __load_modified_directed_graph(self):
        with open(self.__filename, "r") as f:
            line = f.readline().strip()
            if not line:
                raise RepoException("Invalid file.")
            elems = line.split(";")
            if len(elems) != 2:
                raise RepoException("Invalid file.")
            try:
                n = int(elems[0])
                m = int(elems[1])
            except:
                raise RepoException("Invalid file.")

            graph = Graph()
            i = 0
            while i < m:
                line = f.readline()
                line = line.strip()
                if line:
                    a = line.split(";")
                    if len(elems) != 2 and len(elems) != 3:
                        raise RepoException("Invalid file.")
                    try:
                        x = int(a[0])
                        y = int(a[1])
                        try:
                            graph.addVertex(x)
                        except ValidException:
                            pass
                        try:
                            graph.addVertex(y)
                        except ValidException:
                            pass
                        graph.addEdge(x, y)
                        try:
                            c = int(a[2])
                            graph.addCost(x, y, c)
                        except:
                            pass
                    except:
                        raise RepoException("Invalid file.")
                    i += 1

            if i < m:
                raise RepoException("Invalid file.")
            for line in f.readlines():
                line = line.strip()
                if line:
                    try:
                        v = int(line)
                        graph.addVertex(v)
                    except:
                        raise RepoException("Invalid file.")

            self.__elems.clear()
            self.add(graph)


    def __load_undirected_graph(self):
        with open(self.__filename, "r") as f:
            line = f.readline().strip()
            if not line:
                raise RepoException("Invalid file.")
            elems = line.split(";")
            if len(elems) != 2:
                raise RepoException("Invalid file.")
            try:
                n = int(elems[0])
                m = int(elems[1])
            except:
                raise RepoException("Invalid file.")

            graph = Graph()
            i = 0
            while i < m:
                line = f.readline()
                line = line.strip()
                if line:
                    a = line.split(";")
                    if len(elems) != 2 and len(elems) != 3:
                        raise RepoException("Invalid file.")
                    try:
                        x = int(a[0])
                        y = int(a[1])
                        try:
                            graph.addVertex(x)
                        except ValidException:
                            pass
                        try:
                            graph.addVertex(y)
                        except ValidException:
                            pass
                        try:
                            graph.addEdge(x, y)
                            graph.addEdge(y, x)
                        except ValidException:
                            pass
                        try:
                            c = int(a[2])
                            graph.addCost(x, y, c)
                        except:
                            pass
                    except:
                        raise RepoException("Invalid file.")
                    i += 1

            if i < m:
                raise RepoException("Invalid file.")
            for line in f.readlines():
                line = line.strip()
                if line:
                    try:
                        v = int(line)
                        graph.addVertex(v)
                    except:
                        raise RepoException("Invalid file.")

            self.__elems.clear()
            self.add(graph)
