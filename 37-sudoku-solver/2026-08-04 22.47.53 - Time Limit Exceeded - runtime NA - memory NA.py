class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isValid(row, col, num):
            # Check row
            for j in range(9):
                if board[row][j] == num:
                    return False

            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check 3x3 subgrid
            startRow = 3 * (row // 3)
            startCol = 3 * (col // 3)

            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == num:
                        return False

            return True

        def solve():
            for row in range(9):
                for col in range(9):

                    if board[row][col] == ".":

                        for num in "123456789":

                            if isValid(row, col, num):
                                board[row][col] = num

                                if solve():
                                    return True

                                # Backtrack
                                board[row][col] = "."

                        return False

            return True

        solve()