class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]
        
        res, path = [], []

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return
            
            for end in range(start+1, len(s)+1):
                sub_str = s[start:end]
                if not is_palindrome(sub_str):
                    continue
                
                path.append(sub_str)
                backtrack(end)
                path.pop()
        

        backtrack(0)
        return res