class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def climb(n):
            if n in mem:
                return mem[n]
            
            if n == 1 or n == 2:
                return n
            
            res = climb(n-1) + climb(n-2)

            mem[n] = res
            return res
        
        return climb(n)