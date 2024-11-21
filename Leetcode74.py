from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        
        # Binary search on the "flattened" matrix
        left, right = 0, rows * cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Convert 1D index to 2D indices
            row, col = divmod(mid, cols)
            mid_value = matrix[row][col]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
