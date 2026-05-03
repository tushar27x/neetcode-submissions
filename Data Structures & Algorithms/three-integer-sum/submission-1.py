class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans: list[list[int]] = []
        n: int = len(nums)
        nums.sort()
        for i in range(n):
            a = nums[i]
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            
            l = i+1
            h = n-1
            while l<h:
                curr_sum = a + nums[l] + nums[h]

                if curr_sum == 0:
                    ans.append([a,nums[l],nums[h]])
                    l += 1
                    h -= 1
                    while nums[l] == nums[l-1] and l < h:
                        l += 1
                elif curr_sum > 0:
                    h -= 1
                else :
                    l += 1
        
        return ans