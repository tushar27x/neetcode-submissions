class Solution:
    def rev(self, start: int, end: int, nums: List[int]) -> None:
        while start <= end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp

            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.rev(0,n-k-1, nums)
        self.rev(n-k, n-1, nums)
        self.rev(0, n-1, nums)
        