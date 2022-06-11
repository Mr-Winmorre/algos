class BellmanFordGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Add edge
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    # Print the solution
    def print_solution(self, dist):
        print("Vertex Distance from source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):
        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        print(dist)
        # Mark the source vertex
        dist[src] = 0
        # Relax edges |V| - 1 times
        print(self.graph)
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        # step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative cycle found
        # print the distnace and predecessor array
        self.print_solution(dist)
