class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, paths = [], []
        def backtrack(start):
            res.append(paths[:])
            for i in range(start, len(nums)):
                paths.append(nums[i])
                backtrack(i+1)
                paths.pop()
        
        backtrack(0)
        return res