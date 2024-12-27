import sys

def tsp(graph):
    n = len(graph)
    memo = {}

    def tsp_helper(curr, visited):
        if (curr, visited) in memo:
            return memo[(curr, visited)]

        if visited == (1 << n) - 1:
            return (graph[curr][0], [0])

        min_cost = sys.maxsize
        min_path = []
        for next_node in range(n):
            if not visited & (1 << next_node):
                next_cost, next_path = tsp_helper(next_node, visited | (1 << next_node))
                cost = graph[curr][next_node] + next_cost
                if cost < min_cost:
                    min_cost = cost
                    min_path = [next_node] + next_path

        memo[(curr, visited)] = (min_cost, min_path)
        return memo[(curr, visited)]

    min_cost, min_path = tsp_helper(0, 1)
    return min_cost, [0] + min_path

# Example usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost, path = tsp(graph)
if min_cost is None:
    print("No Hamiltonian cycle exists.")
else:
    print("Minimum cost:", min_cost)
    print("Path:", path)