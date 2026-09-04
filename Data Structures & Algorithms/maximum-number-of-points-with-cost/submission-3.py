class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m,n = len(points), len(points[0])
        mem = {}
        def dfs(r,c):
            if (r,c) in mem:
                return mem[(r,c)]

            if r == m-1:
                return 0
            
            res = 0
            for col in range(n):
                res = max(res, points[r+1][col] - abs(col - c) + dfs(r+1,col))

            mem[(r,c)] = res
            return res

        ans = 0
        for c in range(n):
            ans = max(ans, points[0][c] + dfs(0, c))
        
        return ans