class Solution:
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        # Flags to indicate if the first row and column should be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Mark zeroes in the first row and column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark row
                    matrix[0][j] = 0  # Mark column

        # Set zeroes based on marks in the first row and column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Handle the first row
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Handle the first column
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0
