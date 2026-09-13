class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0 

        rows, columns = len(grid), len(grid[0])
        # print(rows, columns)
        island_cnt = 0

        def dfs(row, col):

            # print(row, col)

            if row < 0 or row >= rows or col < 0 or col >= columns or grid[row][col] == "0":
                return 
            
            grid[row][col] = "0" 
            
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)

            return 
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                # print(row, col)

                if grid[row][col] == "1":
                    island_cnt += 1
                
                    dfs(row, col)
        
        return island_cnt

