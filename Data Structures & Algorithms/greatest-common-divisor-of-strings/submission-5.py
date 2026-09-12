class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)
        def isDivide(l):
            if l1%l != 0 and l2%l != 0:
                return False
            n1, n2 = l1 // l, l2 // l

            return str1[:l] * n1 == str1 and str1[:l] * n2 == str2

        max_len = min(l1,l2)
        for i in range(max_len, 0 , -1):
            if isDivide(i):
                return str1[:i]
        
        return ""