class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        nums.sort()
        n = len(nums)
        used = [False] * n 
        def backtrack(n):
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                    
                path.append(nums[i])
                used[i] = True
                backtrack(n)
                path.pop()
                used[i] = False

        backtrack(len(nums))
        return res