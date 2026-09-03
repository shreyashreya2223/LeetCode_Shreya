class Solution:
    def calcEquation(self, equations, values, queries):

        graph = {}

        # Build the graph
        for (a, b), value in zip(equations, values):

            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []

            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(current, target, visited):

            if current == target:
                return 1.0

            visited.add(current)

            for neighbor, weight in graph[current]:

                if neighbor not in visited:

                    result = dfs(neighbor, target, visited)

                    if result != -1.0:
                        return weight * result

            return -1.0

        answers = []

        for start, end in queries:

            if start not in graph or end not in graph:
                answers.append(-1.0)

            else:
                answers.append(dfs(start, end, set()))

        return answers