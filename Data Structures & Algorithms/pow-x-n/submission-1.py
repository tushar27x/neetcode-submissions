class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x: int, n: int) -> float:
            if n == 0: return 1
            if x == 0: return 0

            res = helper(x, n//2)
            res = res * res
            return res*x if n%2 else res
        
        ans = helper(x,abs(n))
        return ans if n > 0 else 1/ans