class Solution:
    def rob(self, nums: List[int]) -> int:
        nxt1, nxt2 = 0,0
        for i in range(len(nums)-1, -1, -1):
            nxt1,nxt2 = max(nxt1, nums[i]+nxt2), nxt1
        
        return nxt1