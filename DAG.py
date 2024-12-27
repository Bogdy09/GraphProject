from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, cost):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append((v, cost))

    def topological_sort(self):
        in_degree = {v: 0 for v in self.adj_list}
        for u in self.adj_list:
            for v, _ in self.adj_list[u]:
                in_degree[v] += 1

        queue = deque()
        for v, degree in in_degree.items():
            if degree == 0:
                queue.append(v)

        top_order = []
        while queue:
            u = queue.popleft()
            top_order.append(u)
            if u in self.adj_list:
                for v, _ in self.adj_list[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)

        if len(top_order) != len(self.adj_list):
            return None
        return top_order

    def highest_cost_path(self, start, end):
        top_order = self.topological_sort()
        if top_order is None:
            return "Graph is not a DAG"

        dist = {v: float('-inf') for v in self.adj_list}
        dist[start] = 0
        predecessor = {v: None for v in self.adj_list}

        for u in top_order:
            if u == end:
                break
            if u in self.adj_list:
                for v, cost in self.adj_list[u]:
                    if dist[v] < dist[u] + cost:
                        dist[v] = dist[u] + cost
                        predecessor[v] = u

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessor[current]
        path.reverse()

        return dist[end], path

def main():
    graph = Graph()
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 3, 6)
    graph.add_edge(2, 3, 2)
    graph.add_edge(3, 4, 7)
    graph.add_edge(5, 4, 20)
    graph.add_edge(3, 5, 5)

    print("Topological sorting:", graph.topological_sort())
    print("Highest cost path from 0 to 4:", graph.highest_cost_path(0, 4))

if __name__ == "__main__":
    main()
