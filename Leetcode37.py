from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def isValid(board, row, col, num):
            # Check row
            for c in range(9):
                if board[row][c] == num:
                    return False
            
            # Check column
            for r in range(9):
                if board[r][col] == num:
                    return False
            
            # Check 3x3 box
            startRow, startCol = 3 * (row // 3), 3 * (col // 3)
            for r in range(startRow, startRow + 3):
                for c in range(startCol, startCol + 3):
                    if board[r][c] == num:
                        return False
            
            return True
        
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num in map(str, range(1, 10)):  # Try '1' to '9'
                            if isValid(board, i, j, num):
                                board[i][j] = num
                                if solve():  # Recursively try to solve the next cells
                                    return True
                                board[i][j] = '.'  # Backtrack
                        return False  # Trigger backtracking
            return True
        
        solve()
