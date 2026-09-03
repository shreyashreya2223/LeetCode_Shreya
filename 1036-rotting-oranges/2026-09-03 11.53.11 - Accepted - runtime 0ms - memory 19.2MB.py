from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])

        q = deque()
        fresh = 0

        # Put all rotten oranges in queue
        # and count fresh oranges
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while q and fresh > 0:
            # Process all oranges that are rotten
            # at the current minute
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] == 1):

                        # Make fresh orange rotten
                        grid[nr][nc] = 2
                        fresh -= 1

                        q.append((nr, nc))

            minutes += 1

        # If fresh oranges remain, they cannot be reached
        if fresh > 0:
            return -1

        return minutes