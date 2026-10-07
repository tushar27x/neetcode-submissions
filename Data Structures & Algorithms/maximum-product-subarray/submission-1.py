class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax, currMin = 1, 1
        for x in nums:
            tmp = currMax * x
            currMax = max(x, currMax*x, currMin*x)
            currMin = min(currMin*x, tmp, x)
            res = max(currMax, res)
        
        return res