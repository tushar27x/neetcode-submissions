class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        mem = [[-1] * m for _ in range(n)]

        def rec(i,j):
            if i == n:
                return True
            if j == m:
                return False
            
            if mem[i][j] != -1:
                return mem[i][j] == 1
            
            if s[i] == t[j]:
                mem[i][j] = 1 if rec(i+1, j+1) else 0
            
            else:
                mem[i][j] = 1 if rec(i, j+1) else 0
            
            return mem[i][j] == 1
        
        return rec(0,0)