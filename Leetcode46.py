class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # Helper function for backtracking
        def backtrack(current):
            # If the current permutation has all elements, add it to the result
            if len(current) == len(nums):
                result.append(list(current))
                return
            
            for num in nums:
                # Skip if the number is already in the current permutation
                if num in current:
                    continue
                # Otherwise, add the number to the current permutation
                current.append(num)
                # Recur with the updated current list
                backtrack(current)
                # Backtrack by removing the last number
                current.pop()
        
        # Start the backtracking process
        backtrack([])
        
        return result
