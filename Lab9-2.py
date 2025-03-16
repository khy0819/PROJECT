import heapq

class Node:
    def __init__(self, number, distance):
        self.number = number
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {i: [] for i in range(self.V + 1)}  # Adjust range to accommodate 1-based indexing

    def add_edge(self, u, v, w):
        self.graph[u].append(Edge(u, v, w))
        self.graph[v].append(Edge(v, u, w))

    def prim_mst(self):
        key = [float('inf')] * (self.V + 1)  # Adjust range to accommodate 1-based indexing
        parent = [None] * (self.V + 1)  # Adjust range to accommodate 1-based indexing
        mst_set = [False] * (self.V + 1)  # Adjust range to accommodate 1-based indexing

        key[1] = 0
        priority_queue = []
        heapq.heappush(priority_queue, Node(1, 0))

        while priority_queue:
            u = heapq.heappop(priority_queue).number
            mst_set[u] = True

            for edge in self.graph[u]:
                v = edge.v
                weight = edge.weight
                if not mst_set[v] and key[v] > weight:
                    key[v] = weight
                    parent[v] = u
                    heapq.heappush(priority_queue, Node(v, key[v]))

        self.print_mst(parent)

    def print_mst(self, parent):
        print("#1 출력")
        for i in range(1, self.V + 1):  # Adjust range to accommodate 1-based indexing
            if parent[i] is not None:
                for edge in self.graph[i]:
                    if edge.v == parent[i]:
                        print(f"{parent[i]} --- {i} : {edge.weight}")


# Example Usage:

N = 7  # Number of vertices
g = Graph(N)

# Input edges
edges = [
    (1, 2, 11),
    (1, 3, 8),
    (1, 4, 9),
    (2, 4, 13),
    (2, 5, 8),
    (3, 6, 10),
    (4, 6, 5),
    (4, 7, 12),
    (5, 7, 7)
]

# Add edges to the graph
for edge in edges:
    start, end, weight = edge
    g.add_edge(start, end, weight)

# Find and print the Minimum Spanning Tree
g.prim_mst()
