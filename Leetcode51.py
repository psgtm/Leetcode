from collections import defaultdict

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col):
            return not (cols[col] or diagonals[row - col] or anti_diagonals[row + col])

        def place_queen(row, col):
            cols[col] = True
            diagonals[row - col] = True
            anti_diagonals[row + col] = True
            board[row][col] = 'Q'

        def remove_queen(row, col):
            cols[col] = False
            diagonals[row - col] = False
            anti_diagonals[row + col] = False
            board[row][col] = '.'

        def backtrack(row):
            if row == n:
                solutions.append([''.join(r) for r in board])
                return
            for col in range(n):
                if is_safe(row, col):
                    place_queen(row, col)
                    backtrack(row + 1)
                    remove_queen(row, col)

        solutions = []
        board = [['.'] * n for _ in range(n)]
        cols = [False] * n
        diagonals = defaultdict(bool)
        anti_diagonals = defaultdict(bool)
        backtrack(0)
        return solutions
