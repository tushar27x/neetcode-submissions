class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l,r = 0, len(nums)

        while l<=r:
            m = l + ((r-l) // 2)

            if (m -1 < 0 or nums[m] != nums[m-1]) and (m+1 == len(nums) or nums[m] != nums[m+1]):
                return nums[m]
            
            leftSize = m-1 if nums[m-1] == nums[m] else m
            if leftSize%2 :
                r = m-1
            else:
                l = m+1

