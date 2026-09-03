class Solution:
    def minReorder(self, n, connections):

        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = set()

        def dfs(city):
            visited.add(city)
            changes = 0

            for neighbor, needs_change in graph[city]:

                if neighbor not in visited:
                    changes += needs_change
                    changes += dfs(neighbor)

            return changes

        return dfs(0)