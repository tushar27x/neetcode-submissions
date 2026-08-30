class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        def rec(i,j):
            if i == n:
                return True
            if j == m:
                return False
            
            if s[i] == t[j]:
                return rec(i+1, j+1)
            
            return rec(i, j+1)
        
        return rec(0,0)