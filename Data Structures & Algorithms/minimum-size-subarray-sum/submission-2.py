class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        curr_sum = 0
        min_len = float('inf')
        for end in range(len(nums)):
            curr_sum += nums[end]
            
            while curr_sum >= target:
                min_len = int(min(min_len, end-start+1))
                curr_sum -= nums[start]
                start += 1
            

        
        return 0 if min_len == float('inf') else min_len