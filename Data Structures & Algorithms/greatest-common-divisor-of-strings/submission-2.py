class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        max_len = min(len(str1), len(str2))
        gcd = ""
        for i in range(1, max_len+1):
            t = str1[:i]

            if len(str1)%len(t) == 0 and len(str2)%len(t) == 0:
                str1_rep = t * (len(str1) // len(t))
                str2_rep = t * (len(str2) // len(t))

                if str1_rep == str1 and str2_rep == str2:
                    gcd = t
        
        return gcd