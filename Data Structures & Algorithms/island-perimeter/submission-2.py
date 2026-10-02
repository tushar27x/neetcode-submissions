class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        visited = set()
        count = 1
        def dfs(r,c):
            if r<0 or r>=n or c<0 or c>=m or grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0
            
            visited.add((r,c))
            perim = dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1) 
            
            return perim

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    return dfs(i,j)

        return 0
