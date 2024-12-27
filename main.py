import copy
from random import randint


class Graph:
    def __init__(self, nr_of_vertices=0):
        self.__nr_of_vertices = nr_of_vertices
        self.__nr_of_edges = 0
        self.__in_edges = {}
        self.__out_edges = {}
        self.__edges_cost = {}

    def get_neighbors(self, vertex):
        return self.__out_edges.get(vertex, [])

    def set_nr_edges(self, nr_of_edges):
        self.__nr_of_edges = nr_of_edges

    def copy_graph(self):
        g = Graph(self.__nr_of_vertices)
        g.__in_edges = copy.deepcopy(self.__in_edges)
        g.__out_edges = copy.deepcopy(self.__out_edges)
        g.__edges_cost = copy.deepcopy(self.__edges_cost)
        return g

    def set_edge_cost(self, edge_id, cost):
        self.__edges_cost[edge_id] = cost

    def check_if_edge_exists(self, x, y):
        return self.edge_id(x, y) != -1

    def get_edges_number(self):
        return self.__nr_of_edges

    def add_edge(self, start_node, end_node, cost):
        self.add_vertex_in_graph(start_node)
        self.add_vertex_in_graph(end_node)
        self.__in_edges[end_node][start_node] = self.__nr_of_edges
        self.__out_edges[start_node][end_node] = self.__nr_of_edges
        self.__edges_cost[self.__out_edges[start_node][end_node]] = cost
        self.__nr_of_edges += 1

    def remove_vertex(self, v):
        if v in self.__in_edges:
            self.__nr_of_vertices -= 1
            self.__nr_of_edges -= len(self.__in_edges[v]) + len(self.__out_edges[v])
            for x in self.__in_edges[v]:
                del self.__edges_cost[self.__in_edges[v][x]]
                del self.__out_edges[x][v]
            for x in self.__out_edges[v]:
                del self.__edges_cost[self.__out_edges[v][x]]
                del self.__in_edges[x][v]
            del self.__in_edges[v]
            del self.__out_edges[v]

    def add_vertex_in_graph(self, v):
        if not v in self.__in_edges:
            self.__in_edges[v] = {}
            self.__out_edges[v] = {}


    def add_vertex_in_graph1(self, v):
        if not v in self.__in_edges:
            self.__nr_of_vertices+=1
            self.__in_edges[v] = {}
            self.__out_edges[v] = {}

    def get_in_neighbours(self, v):
        return set(self.__in_edges[v].keys())

    def get_out_edges(self):
        return dict(sorted(self.__out_edges.items()))

    def set_vertices_number(self, nr_of_vertices):
        self.__nr_of_vertices = nr_of_vertices

    def get_in_edges(self):
        return dict(sorted(self.__in_edges.items()))

    def get_out_degree(self, v):
        """

        :param v:
        :return:
        """
        if v in self.__out_edges:
            return len(self.__out_edges[v])

    def get_out_neighbours(self, v):
        return set(self.__out_edges[v].keys())

    def get_unique_vertices(self):
        return set(self.__in_edges.keys())

    def get_points_of_edge(self, edge_id):
        for x in self.__out_edges:
            for y in self.__out_edges[x]:
                if self.__out_edges[x][y] == edge_id:
                    return x, y
        return -1, -1

    def edge_id(self, x, y):
        if x in self.__out_edges and y in self.__out_edges[x]:
            return self.__out_edges[x][y]
        return -1

    def get_in_degree(self, v):
        if v in self.__in_edges:
            return len(self.__in_edges[v])

    def get_edge_cost(self, edge_id):
        return self.__edges_cost[edge_id]

    def change_edge_cost(self, edge_id, cost):
        self.__edges_cost[edge_id] = cost

    def remove_edge(self, start_node, end_node):
        if self.check_if_edge_exists(start_node, end_node):
            del self.__edges_cost[self.__out_edges[start_node][end_node]]
            del self.__out_edges[start_node][end_node]
            del self.__in_edges[end_node][start_node]
            self.__nr_of_edges -= 1

    def get_vertices_number(self):
        return self.__nr_of_vertices
