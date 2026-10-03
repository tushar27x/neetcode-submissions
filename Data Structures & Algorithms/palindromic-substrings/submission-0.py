class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []

        def expand(l,r):
            while l>=0 and r < len(s) and s[l] == s[r]:
                substr = s[l:r+1]
                res.append(substr)
                l-=1
                r+=1
        
        for i in range(len(s)):
            expand(i,i)
            expand(i, i+1)
        
        return len(res)