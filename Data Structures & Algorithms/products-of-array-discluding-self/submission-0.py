class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans: List[int] = [1] * len(nums)
        prefix: int = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        
        suffix: int = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        return ans