class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D array with dimensions m x n, filled with 1s
        dp = [[1] * n for _ in range(m)]
        
        # Populate dp array by adding the number of ways from the top and left cells
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        # The bottom-right cell contains the total number of unique paths
        return dp[m - 1][n - 1]
