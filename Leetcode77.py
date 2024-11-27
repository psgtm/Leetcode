from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # To store the final combinations

        def backtrack(start, path):
            # If the current combination is of the desired length, add it to the result
            if len(path) == k:
                result.append(path[:])  # Make a copy of path
                return
            
            # Explore further numbers
            for i in range(start, n + 1):
                path.append(i)         # Add the current number to the combination
                backtrack(i + 1, path) # Recurse to the next level
                path.pop()             # Remove the last number to backtrack

        backtrack(1, [])
        return result
