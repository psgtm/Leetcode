from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize max_sum with the first element and current_sum to 0
        max_sum = nums[0]
        current_sum = 0
        
        for num in nums:
            # If current_sum is negative, reset it to 0 (start a new subarray)
            if current_sum < 0:
                current_sum = 0
            # Add the current number to current_sum
            current_sum += num
            # Update max_sum if current_sum is higher
            max_sum = max(max_sum, current_sum)
        
        return max_sum
