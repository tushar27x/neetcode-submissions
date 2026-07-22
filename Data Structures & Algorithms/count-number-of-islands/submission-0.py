class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited_set = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if (r<0 or r >=rows or c < 0 or c >= cols or (r,c) in visited_set or grid[r][c] == "0"):
                return
            
            visited_set.add((r,c))

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited_set:
                    count += 1
                    dfs(i,j)

        return count