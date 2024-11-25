from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Append the current subset to the result
            result.append(path[:])
            # Explore further subsets
            for i in range(start, len(nums)):
                # Include nums[i] in the subset
                path.append(nums[i])
                # Recurse to generate subsets with nums[i] included
                backtrack(i + 1, path)
                # Backtrack by removing nums[i]
                path.pop()
        
        result = []
        backtrack(0, [])
        return result
