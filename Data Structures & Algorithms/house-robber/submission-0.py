class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def check(i):
            if i in dp:
                return dp[i]

            if i >= len(nums):
                return 0
            
            res = max(check(i+1), nums[i] + check(i+2))
            dp[i] = res
            return res
        
        return check(0)