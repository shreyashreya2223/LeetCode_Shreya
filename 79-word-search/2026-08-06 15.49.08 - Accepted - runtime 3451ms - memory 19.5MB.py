class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # All characters matched
            if i == len(word):
                return True

            # Out of bounds or character mismatch
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != word[i]):
                return False

            # Mark as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore 4 directions
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # Backtrack
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False