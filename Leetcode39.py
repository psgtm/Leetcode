class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        # Helper function for backtracking
        def backtrack(remain, comb, start):
            if remain == 0:
                # If the remain is 0, we found a valid combination
                result.append(list(comb))
                return
            elif remain < 0:
                # If the remain is negative, no valid combination
                return
            
            for i in range(start, len(candidates)):
                # Add the candidate to the current combination
                comb.append(candidates[i])
                # Recur with updated remain and the same i (because we can reuse elements)
                backtrack(remain - candidates[i], comb, i)
                # Backtrack by removing the last element from comb
                comb.pop()
        
        # Start the backtracking process
        backtrack(target, [], 0)
        
        return result
