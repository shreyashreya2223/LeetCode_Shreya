# Q7. Course Schedule II
# Time: O(V + E) | Space: O(V + E)

from collections import deque

def findOrder(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1

    queue = deque(
        course for course in range(numCourses)
        if indegree[course] == 0
    )

    order = []

    while queue:
        course = queue.popleft()
        order.append(course)

        for next_course in graph[course]:
            indegree[next_course] -= 1

            if indegree[next_course] == 0:
                queue.append(next_course)

    return order if len(order) == numCourses else []


# Example:
# print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
# One valid output: [0, 2, 1, 3]
