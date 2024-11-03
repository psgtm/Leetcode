from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # Keeps track of the maximum index we can reach
        for i, jump in enumerate(nums):
            if i > max_reach:
                # If the current index is beyond the furthest we can reach, return False
                return False
            max_reach = max(max_reach, i + jump)  # Update the furthest reachable index
            if max_reach >= len(nums) - 1:
                # If we can reach or exceed the last index, return True
                return True
        return True
