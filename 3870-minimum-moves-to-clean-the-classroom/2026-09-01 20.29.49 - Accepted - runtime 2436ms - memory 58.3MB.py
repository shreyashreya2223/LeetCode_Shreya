from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        # Find S and assign an index to every L
        start = None
        litter = {}

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        total_litter = len(litter)
        target = (1 << total_litter) - 1

        # BFS state:
        # (row, col, remaining_energy, mask)
        queue = deque()
        queue.append((start[0], start[1], energy, 0))

        # visited[r][c][mask] = maximum energy
        # with which we have already reached this state.
        #
        # If we reach the same (r,c,mask) with less/equal energy,
        # that state is useless.
        visited = {}

        visited[(start[0], start[1], 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        moves = 0

        while queue:
            for _ in range(len(queue)):
                r, c, curr_energy, mask = queue.popleft()

                # All litter collected
                if mask == target:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # Moving costs 1 energy
                    new_energy = curr_energy - 1

                    # We cannot make a move if we have no energy
                    if new_energy < 0:
                        continue

                    # Collect litter if present
                    new_mask = mask

                    if (nr, nc) in litter:
                        bit = litter[(nr, nc)]
                        new_mask |= (1 << bit)

                    # Reset energy on R
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    # If energy becomes 0, we can only continue
                    # if we are standing on R (because it resets there).
                    if new_energy == 0 and classroom[nr][nc] != 'R':
                        # We can still arrive here, but we cannot make
                        # another move from here.
                        pass

                    state = (nr, nc, new_mask)

                    # If we've reached the same position with the same
                    # mask before with >= energy, this state is dominated.
                    if state in visited and visited[state] >= new_energy:
                        continue

                    visited[state] = new_energy
                    queue.append((nr, nc, new_energy, new_mask))

            moves += 1

        return -1