
from main import Graph
from collections import deque



class ShortestPathFinder:
    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, start_vertex, end_vertex):
        if start_vertex == end_vertex:
            return [start_vertex]

        visited = set()
        queue = deque([(start_vertex, [])])

        while queue:
            current_vertex, path = queue.popleft()
            visited.add(current_vertex)

            for neighbor in self.graph.get_neighbors(current_vertex):
                if neighbor == end_vertex:
                    return path + [current_vertex, neighbor]
                if neighbor not in visited:
                    queue.append((neighbor, path + [current_vertex]))

        return None

# Example usage:
if __name__ == "__main__":
    g = Graph(6)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(3, 4, 1)
    g.add_edge(4, 5, 2)
    g.add_edge(3, 5, 1)
    g.add_edge(2, 6, 1)
    g.add_edge(6, 5, 1)

    shortest_path_finder = ShortestPathFinder(g)
    path = shortest_path_finder.shortest_path(0, 5)
    if path:
        print("Shortest path:", path)
    else:
        print("No path found between the given vertices.")