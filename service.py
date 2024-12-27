from main import Graph
from random import randint


class Service:
    def __init__(self):
        """
        Default constructor of our service. It initializes the following fields:

        self.graph: the graph that we will use for our algorithms
        """
        self.graph = Graph()

    def read_file(self, filename="graph.txt"):
        """
        Reads the content of the file and adds the edges to the graph
        """
        file = open(filename, "r")
        v, e = file.readline().split()
        v, e = int(v), int(e)
        self.graph = Graph(v)
        for i in range(e):
            edge_id = i
            cost = 0
            start_node, end_node, cost = file.readline().split()
            start_node, end_node, cost = int(start_node), int(end_node), int(cost)
            self.graph.add_edge(start_node, end_node, cost)

    def write_file(self, filename):
        """
        Writes the graph in a file
        """
        file = open(filename, "w")
        file.write(str(self.graph.get_vertices_number()) + " " + str(self.graph.get_edges_number()) + "\n")
        out_edges = self.graph.get_out_edges()
        for x in out_edges:
            for y in out_edges[x]:
                file.write(str(x) + " " + str(y) + " " + str(self.graph.get_edge_cost(out_edges[x][y])) + "\n")

    def generate_random_graph(self, nr_of_vertices, nr_of_edges):
        """
        Generates a random graph
        :param nr_of_vertices: the number of vertices of the graph
        :param nr_of_edges: the number of edges of the graph
        """
        self.graph = Graph(nr_of_vertices)
        for i in range(nr_of_edges):
            start_node = randint(0, nr_of_vertices - 1)
            end_node = randint(0, nr_of_vertices - 1)
            while self.graph.check_if_edge_exists(start_node, end_node):
                start_node = randint(0, nr_of_vertices - 1)
                end_node = randint(0, nr_of_vertices - 1)
            self.graph.add_vertex_in_graph(start_node)
            self.graph.add_vertex_in_graph(end_node)
            self.graph.add_edge(start_node, end_node, i)
            self.graph.set_edge_cost(i, randint(1, 100) - 50)

