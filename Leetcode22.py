class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s='', left=0, right=0):
            # If the string is of length 2 * n, we've formed a valid combination
            if len(s) == 2 * n:
                result.append(s)
                return
            
            # If we can add a '(' (left < n), do so and backtrack
            if left < n:
                backtrack(s + '(', left + 1, right)
            
            # If we can add a ')' (right < left), do so and backtrack
            if right < left:
                backtrack(s + ')', left, right + 1)
        
        result = []
        backtrack()  # Start the backtracking process
        return result
