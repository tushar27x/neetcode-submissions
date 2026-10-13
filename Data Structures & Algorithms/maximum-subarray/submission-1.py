class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum = 0, nums[0]
        for n in nums:
            currSum = max(n, currSum + n)
            maxSum = max(maxSum, currSum)

        return maxSum 