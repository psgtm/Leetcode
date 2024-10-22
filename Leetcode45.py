from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize variables
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We don't need to consider the last index in the loop since we must stop before it
        for i in range(len(nums) - 1):
            # Update the farthest we can reach from the current position
            farthest = max(farthest, i + nums[i])
            
            # If we have reached the end of the current jump range, we need another jump
            if i == current_end:
                jumps += 1
                current_end = farthest
        
        return jumps

# Example usage:
sol = Solution()
print(sol.jump([2, 3, 1, 1, 4]))  # Output: 2
