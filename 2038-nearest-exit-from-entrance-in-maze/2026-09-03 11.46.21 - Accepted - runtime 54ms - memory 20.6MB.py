from collections import deque

class Solution:
    def nearestExit(self, maze, entrance):
        m = len(maze)
        n = len(maze[0])

        q = deque()
        q.append((entrance[0], entrance[1], 0))

        # Mark entrance as visited
        maze[entrance[0]][entrance[1]] = '+'

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        while q:
            r, c, steps = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Check boundaries and whether cell is empty
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':

                    # If it's a border cell, it's an exit
                    if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                        return steps + 1

                    # Mark visited
                    maze[nr][nc] = '+'

                    # Add to BFS
                    q.append((nr, nc, steps + 1))

        return -1