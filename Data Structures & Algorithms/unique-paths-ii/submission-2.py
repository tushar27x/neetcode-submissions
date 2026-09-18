class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(m-1, n-1): 1}
        def dfs(i,j):
            if i >= m or j>=n or obstacleGrid[i][j] == 1:
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]

            res = dfs(i+1, j) + dfs(i, j+1)
            dp[(i,j)] = res
            return res
        
        return dfs(0,0)