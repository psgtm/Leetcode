class Solution:
    def totalNQueens(self, n: int) -> int:
        # Helper function to check if a queen can be placed at (row, col)
        def is_safe(row, col):
            return col not in cols and (row - col) not in diag1 and (row + col) not in diag2

        # Backtracking function
        def backtrack(row):
            # If we've placed queens in all rows, count this configuration
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                if is_safe(row, col):
                    # Place the queen
                    cols.add(col)
                    diag1.add(row - col)
                    diag2.add(row + col)
                    
                    # Recur to place the next queen
                    count += backtrack(row + 1)
                    
                    # Backtrack
                    cols.remove(col)
                    diag1.remove(row - col)
                    diag2.remove(row + col)
            
            return count

        # Sets to keep track of columns and diagonals
        cols = set()
        diag1 = set()  # Top-left to bottom-right diagonals
        diag2 = set()  # Top-right to bottom-left diagonals
        
        # Start the backtracking process
        return backtrack(0)
