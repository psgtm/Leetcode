from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize an n x n matrix with 0s
        matrix = [[0] * n for _ in range(n)]
        
        # Define initial boundary values for rows and columns
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        num = 1  # Start filling with number 1

        while left <= right and top <= bottom:
            # Fill top row
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1  # Move the top boundary down

            # Fill right column
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1  # Move the right boundary left

            # Fill bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1  # Move the bottom boundary up

            # Fill left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1  # Move the left boundary right

        return matrix
