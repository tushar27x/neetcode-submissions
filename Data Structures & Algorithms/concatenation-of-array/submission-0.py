class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        N = 2*n
        ans = [-1] * N
        ans[:n] = [nums[i] for i in range(n)]

        start = n
        while start < N:
            ans[start] = nums[start-n]
            start += 1
        
        return ans