class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def backtrack(x, y, remain):
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == -1:
                return 0
            if grid[x][y] == 2:
                return 1 if remain == 0 else 0
            
            temp = grid[x][y]
            grid[x][y] = -1
            remain -= 1
            
            paths = (
                backtrack(x + 1, y, remain) +
                backtrack(x - 1, y, remain) +
                backtrack(x, y + 1, remain) +
                backtrack(x, y - 1, remain)
            )
            
            grid[x][y] = temp
            remain += 1
            
            return paths

        rows, cols = len(grid), len(grid[0])
        start_x = start_y = 0
        empty_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == 0:
                    empty_count += 1

        return backtrack(start_x, start_y, empty_count + 1)
