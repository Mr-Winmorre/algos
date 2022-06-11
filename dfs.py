class Dfs:
    def dfs(self, graph, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)

        print(start)
        for next in graph[start] - visited:
            self.dfs(graph, next, visited)
        return visited
