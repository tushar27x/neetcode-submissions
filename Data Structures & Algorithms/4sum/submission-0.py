class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                b = nums[j]
                k = j+1
                l = n-1
                while k<l:
                    c = nums[k]
                    d = nums[l]
                    curr_sum = a + b + c + d
                    if curr_sum == target:
                        ans.append([a,b,c,d])
                        while k<l and nums[k] == nums[k+1]:
                            k += 1
                        
                        while k<l and nums[l] == nums[l-1]:
                            l -= 1
                        k += 1
                        l -= 1
                    
                    elif curr_sum < target:
                        k += 1
                    else:
                        l -= 1
                
        return ans