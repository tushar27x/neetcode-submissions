class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        
        have = 0
        required = len(need)
        window={}
        best = ""
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == required:
                if best == "" or right-left+1 < len(best):
                    best = s[left:right+1]
                
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                
                left+=1
            

        return best
        
        