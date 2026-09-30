class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c):
            if r < 0 or r >= n or c < 0 or c >= m or (r,c) in visited or grid[r][c] == '0':
                return
            
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        count = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == '1' and (r,c) not in visited: 
                    count+=1
                    dfs(r,c)
        
        return count