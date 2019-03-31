from domain.graph import ValidException
from repo.repository import RepoException
from service.ctrl import CtrlException


class Console():
    def __init__(self, ctrl):
        self.__ctrl = ctrl
        self.__commands = {
            '0': [exit, "\n 0.Exit."],
            '1': [self.__ui_save_graph, " 1.Save graph to file."],
            '2': [self.__ui_load_big_graph, " 2.Load big directed graph from file."],
            '3': [self.__ui_load_modified_graph, " 3.Load modified directed graph from file."],
            '4': [self.__ui_load_undirected_graph, " 4.Load undirected graph from file."],
            '5': [self.__number_of_vertices, " 5.The number of vertices."],
            '6': [self.__number_of_edges, " 6.The number of edges."],
            '7': [self.__is_edge, " 7.Is edge."],
            '8': [self.__is_vertex, " 8.Is vertex."],
            '9': [self.__in_degree, " 9.The inDegree of a vertex."],
            '10': [self.__out_degree, "10.The outDegree of a vertex."],
            '11': [self.__print_graph, "11.Print graph."],
            '12': [self.__list_vertices, "12.List all vertices."],
            '13': [self.__list_all_edges, "13.List all edges."],
            '14': [self.__list_in_edges_vertex, "14.List inbound edges of a given vertex."],
            '15': [self.__list_out_edges_vertex, "15.List outbound edges of a given vertex."],
            '16': [self.__print_cost_of_edge, "16.Print the cost of an edge."],
            '17': [self.__add_vertex, "17.Add new vertex."],
            '18': [self.__add_edge, "18.Add new edge."],
            '19': [self.__add_cost, "19.Add cost to an edge."],
            '20': [self.__update_cost, "20.Update the cost of an edge."],
            '21': [self.__remove_cost, "21.Remove the cost of an edge."],
            '22': [self.__remove_edge, "22.Remove edge."],
            '23': [self.__remove_vertex, "23.Remove vertex."],
            '24': [self.__get_strongly_connected_components_dfs,
                   "24.Get the strongly connected components by using depth first search."],
            '25': [self.__find_lowest_cost_walk,
                   "25.Find the lowest cost walk between two vertices."],
            '26': [self.__minimal_spanning_tree_kruskal,
                   "26.Find a minimum spanning tree of the graph, using Kruskal's algorithm."],
            '27': [self.__find_vertex_cover,
                   "27.Find a vertex cover of no more than twice the optimal number of vertices.\n"]
        }


    def __read_int(self, text):
        while True:
            try:
                return int(input(text))
            except:
                print("Invalid number.")


    def __show_menu(self):
        for command in self.__commands.values():
            print(command[1])


    def __time(self):
        return "The time used to perform this operation is: " + str(self.__ctrl.get_time())


    def __print_list(self, entities):
        for entity in entities:
            print(entity)


    def run(self):
        print("--- Welcome to Graph (version) 1.0! ---")
        print("This is an empty graph. :)")
        print("Add some vertices, or load an existing graph from a file.")
        while True:
            self.__show_menu()
            try:
                cmd = input(">> ")
                if not cmd:
                    print("Invalid command.")
                elif cmd == '0':
                    exit(0)
                elif cmd in self.__commands:
                    self.__commands[cmd][0]()
                    print(self.__time())
                else:
                    print("Please write a valid command.")
            # except ValidException as e:
            #     print(e)
            # except RepoException as e:
            #     print(e)
            except CtrlException as e:
                print(e)


    def __ui_save_graph(self):
        filename = input("Enter filename: ")
        if not filename:
            print("Invalid filename.")
            self.__ui_save_graph()
        self.__ctrl.save_file(filename)
        print("Graph successfully saved to the file \'" + filename + "\'.")


    def __ui_load_big_graph(self):
        filename = input("Enter filename: ")
        if not filename:
            print("Invalid filename")
            self.__ui_load_big_graph()
        self.__ctrl.load_file(filename)
        print("The current graph is from the file \'" + filename + "\'.")


    def __ui_load_modified_graph(self):
        filename = input("Enter filename: ")
        if not filename:
            print("Invalid filename")
            self.__ui_load_modified_graph()
        self.__ctrl.load_modified_graph(filename)
        print("The current graph is from the file \'" + filename + "\'.")


    def __ui_load_undirected_graph(self):
        filename = input("Enter filename: ")
        if not filename:
            print("Invalid filename")
            self.__ui_load_undirected_graph()
        self.__ctrl.load_undirected_graph(filename)
        print("The current graph is from the file \'" + filename + "\'.")


    def __add_vertex(self):
        vertex = self.__read_int("Vertex: ")
        self.__ctrl.add_vertex(vertex)
        print("The vertex " + str(vertex) + " was successfully added.")


    def __add_edge(self):
        x = self.__read_int("Starting vertex: ")
        y = self.__read_int("End point: ")
        self.__ctrl.add_edge(x, y)
        print("The edge (" + str(x) + ", " + str(y) + ") was successfully added.")


    def __add_cost(self):
        x = self.__read_int("Starting vertex: ")
        y = self.__read_int("End point: ")
        cost = self.__read_int("Cost: ")
        self.__ctrl.add_cost(x, y, cost)
        print("The cost " + str(cost) + " was successfully added to the edge (" + str(x) + ", " + str(y) + ").")


    def __number_of_vertices(self):
        print("There are " + str(self.__ctrl.number_of_vertices()) + " vertices in the graph.")


    def __number_of_edges(self):
        print("There are " + str(self.__ctrl.number_of_edges()) + " edges in the graph.")


    def __in_degree(self):
        vertex = self.__read_int("Vertex: ")
        degree = self.__ctrl.in_degree(vertex)
        print("The inDegree of the vertex " + str(vertex) + " is " + str(degree) + ".")


    def __out_degree(self):
        vertex = self.__read_int("Vertex: ")
        degree = self.__ctrl.out_degree(vertex)
        print("The outDegree of the vertex " + str(vertex) + " is " + str(degree) + ".")


    def __is_edge(self):
        x = self.__read_int("Starting vertex: ")
        y = self.__read_int("End point: ")
        is_edge = self.__ctrl.is_edge(x, y)
        if is_edge:
            print("The edge (" + str(x) + ", " + str(y) + ") exists.")
        else:
            print("The edge (" + str(x) + ", " + str(y) + ") does not exist.")


    def __is_vertex(self):
        vertex = self.__read_int("Vertex: ")
        is_vertex = self.__ctrl.is_vertex(vertex)
        if is_vertex:
            print("The vertex " + str(vertex) + " exists.")
        else:
            print("The vertex " + str(vertex) + " does not exist.")


    def __print_graph(self):
        print(self.__ctrl.print_graph())


    def __list_vertices(self):
        s = self.__ctrl.get_vertices()
        if s:
            print(s)
        else:
            print("No vertices in the graph.")


    def __list_all_edges(self):
        s = self.__ctrl.get_all_edges()
        if s:
            print(s)
        else:
            print("No edges in the graph.")


    def __list_in_edges_vertex(self):
        vertex = self.__read_int("Vertex: ")
        print(self.__ctrl.get_in_edges_of_vertex(vertex))


    def __list_out_edges_vertex(self):
        vertex = self.__read_int("Vertex: ")
        print(self.__ctrl.get_out_edges_of_vertex(vertex))


    def __update_cost(self):
        x = self.__read_int("Starting vertex: ")
        y = self.__read_int("End point: ")
        cost = self.__read_int("Cost: ")
        self.__ctrl.update_cost(x, y, cost)
        print("The cost of the edge (" + str(x) + ", " + str(y) + ") was successfully updated with the new value: " +
              str(cost) + ".")


    def __remove_cost(self):
        x = self.__read_int("Starting vertex: ")
        y = self.__read_int("End point: ")
        self.__ctrl.remove_cost(x, y)
        print("The cost of the edge (" + str(x) + ", " + str(y) + ") was successfully removed.")


    def __remove_edge(self):
        x = self.__read_int("Starting vertex: ")
        y = self.__read_int("End point: ")
        self.__ctrl.remove_edge(x, y)
        print("The edge (" + str(x) + ", " + str(y) + ") was successfully removed.")


    def __remove_vertex(self):
        vertex = self.__read_int("Vertex: ")
        self.__ctrl.remove_vertex(vertex)
        print("The vertex " + str(vertex) + " and all its edges were successfully removed.")


    def __print_cost_of_edge(self):
        x = self.__read_int("Starting vertex: ")
        y = self.__read_int("End point: ")
        cost = self.__ctrl.get_cost(x, y)
        print("The cost of the edge (" + str(x) + ", " + str(y) + ") is " + str(cost) + ".")


    def __get_strongly_connected_components_dfs(self):
        self.__ctrl.get_strongly_connected_components_by_dfs()


    def __find_lowest_cost_walk(self):
        x = self.__read_int("Starting vertex: ")
        y = self.__read_int("End point: ")
        dist, walk = self.__ctrl.find_lowest_cost_walk(x, y)
        print("The cost of the walk is " + str(dist) + ". Verteces: " + str(walk) + ".")


    def __minimal_spanning_tree_kruskal(self):
        filename = input("Output filename: ")
        self.__ctrl.minimal_spanning_tree_kruskal(filename)
        print("The new graph was successfully added to the file " + filename + ".")


    def __find_vertex_cover(self):
        print("The vertex cover is: " + str(self.__ctrl.find_vertex_cover()))
