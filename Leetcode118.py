from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize an empty list to hold the triangle
        triangle = []

        # Generate each row
        for i in range(numRows):
            # Start each row with '1'
            row = [1] * (i + 1)

            # Compute the values between the 1's
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            # Add the current row to the triangle
            triangle.append(row)

        return triangle
