from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate the width and height for the current container
            width = right - left
            current_height = min(height[left], height[right])
            
            # Calculate the current area
            current_area = width * current_height
            
            # Update max_area if current_area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer that points to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
