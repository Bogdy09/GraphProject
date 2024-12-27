class Graph:
    def __init__(self, nr_of_vertices=0):
        self.__nr_of_vertices = nr_of_vertices
        self.__edges_cost = {}
        self.__in_edges = {i: {} for i in range(nr_of_vertices)}
        self.__out_edges = {i: {} for i in range(nr_of_vertices)}

    def add_edge(self, start_node, end_node, cost):
        self.__out_edges[start_node][end_node] = cost
        self.__in_edges[end_node][start_node] = cost
        self.__edges_cost[(start_node, end_node)] = cost

    def get_vertices(self):
        return list(self.__out_edges.keys())

    def get_nr_of_vertices(self):
        return self.__nr_of_vertices

    def get_edge_cost(self, start_node, end_node):
        return self.__edges_cost.get((start_node, end_node), float('inf'))

    def get_out_edges(self):
        return dict(sorted(self.__out_edges.items()))

    def get_in_edges(self):
        return dict(sorted(self.__in_edges.items()))

class FloydWarshall:
    def __init__(self, graph):
        self.graph = graph
        self.dist = None
        self.next_node = None

    def initialize(self):
        num_vertices = self.graph.get_nr_of_vertices()
        self.dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        self.next_node = [[None] * num_vertices for _ in range(num_vertices)]

        for v in range(num_vertices):
            self.dist[v][v] = 0

        out_edges = self.graph.get_out_edges()
        for u in out_edges:
            for v in out_edges[u]:
                cost = out_edges[u][v]
                self.dist[u][v] = cost
                self.next_node[u][v] = v

    def floyd_warshall(self):
        num_vertices = self.graph.get_nr_of_vertices()
        for k in range(num_vertices):
            for i in range(num_vertices):
                for j in range(num_vertices):
                    if self.dist[i][j] > self.dist[i][k] + self.dist[k][j]:
                        self.dist[i][j] = self.dist[i][k] + self.dist[k][j]
                        self.next_node[i][j] = self.next_node[i][k]

    def construct_path(self, start_node, end_node):
        if self.next_node[start_node][end_node] is None:
            return None
        path = [start_node]
        while start_node != end_node:
            start_node = self.next_node[start_node][end_node]
            path.append(start_node)
        return path

    def get_shortest_path_cost(self, start_node, end_node):
        return self.dist[start_node][end_node]

def create_sample_graph():
    graph = Graph(8)
    graph.add_edge(1, 4, 2)
    graph.add_edge(1, 3, 6)
    graph.add_edge(1, 2, 7)
    graph.add_edge(4, 3, 3)
    graph.add_edge(3, 2, 1)
    graph.add_edge(4, 7, 1)
    graph.add_edge(3, 5, 4)
    graph.add_edge(2, 5, 2)
    graph.add_edge(7, 5, 7)
    graph.add_edge(6, 2, 7)
    graph.add_edge(6, 5, 1)
    return graph

def main():
    graph = create_sample_graph()
    fw_algorithm = FloydWarshall(graph)
    fw_algorithm.initialize()
    fw_algorithm.floyd_warshall()

    start_node = 1
    end_node = 7
    cost = fw_algorithm.get_shortest_path_cost(start_node, end_node)
    if cost == float('inf'):
        print(f"There is no path between vertex {start_node} and vertex {end_node}.")
    else:
        path = fw_algorithm.construct_path(start_node, end_node)
        print(f"The lowest cost walk from {start_node} to {end_node} costs {cost}.")
        print(f"The path is: {' -> '.join(map(str, path))}")

if __name__ == "__main__":
    main()