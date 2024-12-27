from FloydWarshall import FloydWarshall
from service import Service
from main import Graph
from BFS import ShortestPathFinder

class UI:
    def __init__(self):
        """
        Initialize the UI class with a Service instance.
        """
        self.__service = Service()
        self.fw_algorithm = None

    def print_graph(self):
        """
        Print the number of vertices, number of edges, and the details of each edge in the graph.
        """
        print(str(self.__service.graph.get_vertices_number()) + " " + str(self.__service.graph.get_edges_number()))
        out_edges = self.__service.graph.get_out_edges()
        for x in out_edges:
            for y in out_edges[x]:
                print(str(out_edges[x][y]) + ") " + str(x) + " " + str(y) + " " + str(
                    self.__service.graph.get_edge_cost(out_edges[x][y])))

    def print_vertices(self):
        """
        Print all the vertices in the graph.
        """
        vertices = self.__service.graph.get_unique_vertices()
        print("These are the vertices: ")
        for v in vertices:
            print(str(v))

    def check_if_edge_exists(self):
        """
        Check if an edge exists between two given vertices.
        """
        x, y = input("Please enter the 2 vertices: ").split()
        try:
            x, y = int(x), int(y)
        except ValueError:
            print("Invalid input! Please try again!")
            return
        if self.__service.graph.check_if_edge_exists(x, y):
            print("The existing edge is: " + str(x) + "->" + str(y))
        else:
            print("There is no such edge! ")

    def get_in_degree_and_out_degree(self):
        """
        Get the in-degree and out-degree of a given vertex.
        """
        try:
            v = int(input("Please enter the vertex: "))
        except ValueError:
            print("Invalid input! Please try again!")
            return
        print("The in degree of " + str(v) + " is " + str(self.__service.graph.get_in_degree(v)))
        print("The out degree of " + str(v) + " is " + str(self.__service.graph.get_out_degree(v)))

    def parse_outbound_edges(self):
        """
        Parse and print the outbound edges of a given vertex.
        """
        try:
            v = int(input("Please enter the vertex: "))
        except ValueError:
            print("Invalid input! Please try again!")
            return
        out_edges = self.__service.graph.get_out_edges()
        if v in out_edges:
            if len(out_edges[v]) == 0:
                print("There are no outbound edges for " + str(v))
            else:
                print("The outbound edges of " + str(v) + " are: ")
                for y in out_edges[v]:
                    print(str(v) + " " + str(y) + " " + str(out_edges[v][y]))
        else:
            print("There are no outbound edges for " + str(v))

    def parse_inbound_edges(self):
        """
        Parse and print the inbound edges of a given vertex.
        """
        try:
            v = int(input("Please enter the vertex: "))
        except ValueError:
            print("Invalid input!")
            return
        in_edges = self.__service.graph.get_in_edges()
        if v in in_edges:
            if len(in_edges[v]) == 0:
                print("There are no inbound edges for " + str(v))
            else:
                print("The inbound edges of " + str(v) + " are: ")
                for x in in_edges[v]:
                    print(str(x) + " " + str(v) + " " + str(in_edges[v][x]))
        else:
            print("There are no inbound edges for " + str(v))

    def get_endpoints_of_edge(self):
        """
        Get and print the endpoints of a given edge.
        """
        try:
            e = int(input("Please enter the edge: "))
        except ValueError:
            print("Invalid input!")
            return
        x, y = self.__service.graph.get_points_of_edge(e)
        if x == -1:
            print("There is no edge with ID " + str(e))
        else:
            print("The endpoints of edge " + str(e) + " are " + str(x) + " and " + str(y))

    def modify_cost_of_edge(self):
        """
        Modify the cost of a given edge.
        """
        try:
            id = int(input("Cost of which edge do you want to modify? "))
        except ValueError:
            print("Invalid input!")
            return
        try:
            new_cost = int(input("What is the new cost? "))
        except ValueError:
            print("Invalid input!")
            return
        self.__service.graph.set_edge_cost(id, new_cost)
        print("The cost of the edge has been modified to " + str(new_cost))

    def add_edge(self):
        """
        Add an edge to the graph.
        """
        if self.__service.graph.get_vertices_number() == 0:
            print("First, you have to add vertices before you can add an edge!")
            return
        try:
            x, y, cost = input("Please enter the 2 vertices and the cost: ").split()
            x, y, cost = int(x), int(y), int(cost)
        except ValueError:
            print("Invalid input!")
            return
        if x >= self.__service.graph.get_vertices_number() or y >= self.__service.graph.get_vertices_number():
            print("The provided vertices MUST BE between 0 and n - 1. Try again!")
        elif self.__service.graph.check_if_edge_exists(x, y):
            print("There is already an edge from " + str(x) + " to " + str(y))
        else:
            self.__service.graph.add_edge(x, y, cost)
            print("The edge from " + str(x) + " to " + str(y) + " has been added")

    def remove_edge(self):
        """
        Remove an edge from the graph.
        """
        if self.__service.graph.get_vertices_number() == 0:
            print("First, you have to add vertices before you can remove an edge!")
            return
        try:
            x, y = input("Please enter the 2 vertices: ").split()
            x, y = int(x), int(y)
        except ValueError:
            print("Invalid input!")
            return
        if self.__service.graph.check_if_edge_exists(x, y):
            self.__service.graph.remove_edge(x, y)
            print("The edge from " + str(x) + " to " + str(y) + " has been removed!")
        else:
            print("There is no edge from " + str(x) + " to " + str(y))

    """def add_vertex(self):
        
        
        if self.__service.graph.get_vertices_number() == 0:
            try:
                v = int(input("The graph is empty! Please provide the number of vertices first: "))
            except ValueError:
                print("Invalid input!")
                return
            self.__service.graph.set_number_of_vertices(v)
        try:
            v = int(input("Please enter the vertex: "))
        except ValueError:
            print("Invalid input!")
            return
        self.__service.graph.add_vertex(v)
        print("Done!")"""

    def add_vertex(self):
        """
        Menu to add a vertex to the graph. If the graph is empty, the user MUST provide the number of vertices first. In case the user adds a vertex that already exists, the operation will have no effect on the graph.
        """
        if self.__service.graph.get_vertices_number() == 0:
            try:
                v = int(input("The graph is empty! Please provide the number of vertices first: "))
            except ValueError:
                print("Invalid input!")
                return
            self.__service.graph.set_vertices_number(v)
        try:
            v = int(input("Please enter the vertex: "))
        except ValueError:
            print("Invalid input!")
            return
        self.__service.graph.add_vertex_in_graph1(v)
        print("Done!")

    def remove_vertex(self):
        """
        Remove a vertex from the graph.
        """
        try:
            v = int(input("Please enter the vertex: "))
        except ValueError:
            print("Invalid input!")
            return
        self.__service.graph.remove_vertex(v)
        print("Done!")

    def copy_graph(self):
        """
        Create a copy of the graph.
        """
        copy_of_graph = self.__service.graph.copy_graph()
        print("Done!")

    def print_the_cost(self):
        """
        Print the cost of a given edge.
        """
        try:
            id = int(input("Please enter the id of the edge: "))
        except ValueError:
            print("Invalid input!")
            return
        print("The cost of the vertex is " + str(self.__service.graph.get_edge_cost(id)))

    def read_graph_from_file(self):
        """
        Read graph data from a file.
        """
        self.__service.read_file("graph.txt")
        print("Done!")

    def write_graph_to_file(self):
        """
        Write graph data to a file.
        """
        filename = input("Please enter the filename: ")
        self.__service.write_file(filename)
        print("Done!")

    def generate_random_graph(self):
        """
        Generate a random graph.
        """
        try:
            n, m = input("Please enter the number of vertices and edges: ").split()
            n, m = int(n), int(m)
        except ValueError:
            print("Invalid input!")
            return
        self.__service.generate_random_graph(n, m)
        print("Done!")

    def read_graph(self):
        filename = input("Enter the filename of the graph: ")
        with open(filename, "r") as file:
            v, e = map(int, file.readline().split())
            self.graph = Graph(v)
            for _ in range(e):
                start_node, end_node, cost = map(int, file.readline().split())
                self.graph.add_edge(start_node, end_node, cost)
        self.fw_algorithm = FloydWarshall(self.graph)
        self.fw_algorithm.initialize()
        self.fw_algorithm.floyd_warshall()


    def print_menu(self):
        """
        Print the menu options.
        """
        print("Menu:")
        print("1. Get the number of vertices and edges")
        print("2. Print the graph")
        print("3. Find out if there is an edge between two vertices")
        print("4. Get the in degree and out degree of a vertex")
        print("5. Parse the set of outbound edges of a vertex")
        print("6. Parse the set of inbound edges of a vertex")
        print("7. Get the endpoints of an edge")
        print("8. Modify the cost of an edge")
        print("9. Add an edge")
        print("10. Remove an edge")
        print("11. Add a vertex")
        print("12. Remove a vertex")
        print("13. Print vertices of graph")
        print("14. Print the cost of the edge")
        print("15. Copy the graph")
        print("16. Read graph from file")
        print("17. Write graph in file")
        print("18. Generate random graph")
        print("20. Find shortest path")
        print("21. Find lowest cost walk")

    def run(self):
        """
        Run the user interface.
        """
        while True:
            self.print_menu()
            command = input("Please enter a choice: ")
            if command == "1":
                print("The number of vertices is: " + str(self.__service.graph.get_vertices_number()))

                print("The number of edges is: " + str(self.__service.graph.get_edges_number()))
            elif command == "2":
                self.print_graph()
            elif command == "3":
                self.check_if_edge_exists()
            elif command == "4":
                self.get_in_degree_and_out_degree()
            elif command == "5":
                self.parse_outbound_edges()
            elif command == "6":
                self.parse_inbound_edges()
            elif command == "7":
                self.get_endpoints_of_edge()
            elif command == "8":
                self.modify_cost_of_edge()
            elif command == "9":
                self.add_edge()
            elif command == "10":
                self.remove_edge()
            elif command == "11":
                self.add_vertex()
            elif command == "12":
                self.remove_vertex()
            elif command == "13":
                self.print_vertices()
            elif command == "14":
                self.print_the_cost()
            elif command == "15":
                self.copy_graph()
            elif command == "16":
                self.read_graph_from_file()
            elif command == "17":
                self.write_graph_to_file()
            elif command == "18":
                self.generate_random_graph()
            elif command == "20":
                starting_vertex=int(input("Please enter the starting vertex: "))
                ending_vertex = int(input("Please enter the ending vertex: "))

                shortest_path_finder = ShortestPathFinder(self.__service.graph)
                path = shortest_path_finder.shortest_path(starting_vertex, ending_vertex)

                if path:
                    print("Shortest path:", path)
                else:
                    print("No path found between the given vertices.")
            elif command == "21":
                self.find_lowest_cost_walk()
            else:
                print("Invalid choice!. Please try again!")


ui = UI()

ui.run()
