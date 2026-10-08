import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = []
        for n in nums:
            if not tmp or n > tmp[-1]:
                tmp.append(n)
            else:
                idx = bisect.bisect_left(tmp, n)
                tmp[idx] = n 
        
        return len(tmp)