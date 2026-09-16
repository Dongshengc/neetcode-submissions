class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        areas = []
        m, n = len(grid), len(grid[0])

        def dfs(row, col):

            # print(row, col)

            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return 0
            
            cnt = 1
            grid[row][col] = 0

            cnt += dfs(row+1, col)
            cnt += dfs(row-1, col)
            cnt += dfs(row, col+1)
            cnt += dfs(row, col-1)

            return cnt

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    areas.append(dfs(i, j))

        if areas:
            return max(areas)
        else:
            return 0
        