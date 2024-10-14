class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Create a DP table with (len(s) + 1) rows and (len(p) + 1) columns
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: empty string and empty pattern is a match
        dp[0][0] = True
        
        # Fill the dp array for patterns that can match an empty string
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Iterate over the string and the pattern
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # If the current characters match, or the pattern has '.', propagate the match
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                # If we encounter '*', we check two possibilities
                elif p[j - 1] == '*':
                    # Case 1: Treat '*' as matching zero occurrences of the preceding element
                    dp[i][j] = dp[i][j - 2]
                    # Case 2: Treat '*' as matching one or more occurrences, if possible
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        # The result is whether the whole string matches the whole pattern
        return dp[len(s)][len(p)]
