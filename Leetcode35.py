from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize the left and right pointers for binary search
        left, right = 0, len(nums) - 1
        
        # Perform binary search
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # If the target is not found, left will be the insertion point
        return left