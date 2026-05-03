class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n: int = len(heights)
        l: int = 0
        h: int = n-1
        max_vol: int = 0
        while l < h:
            max_vol = max((h-l) * min(heights[h], heights[l]), max_vol)
            if heights[h] > heights[l]:
                l += 1
            else:
                h -= 1
        
        return max_vol