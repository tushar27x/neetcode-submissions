class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(start, end):
            dp = {}
            def check(i):
                if i in dp:
                    return dp[i]

                if i > end:
                    return 0
                
                res = max(check(i+1), nums[i] + check(i+2))
                dp[i] = res
                return res
            
            return check(start)
        
        return max(solve(0, len(nums)-2), solve(1, len(nums)-1))