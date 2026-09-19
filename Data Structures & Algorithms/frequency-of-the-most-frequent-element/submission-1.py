class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_freq,total,i = 0,0,0
        
        for j in range(len(nums)):
            total+=nums[j]
            while nums[j] * (j-i+1) > total+k:
                total -= nums[i]
                i += 1
            
            max_freq = max(max_freq, (j-i+1))
            

        return max_freq


