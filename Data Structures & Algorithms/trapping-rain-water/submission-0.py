class Solution:
    def trap(self, height: List[int]) -> int:
        n: int = len(height)
        l: int = 0
        r: int = n-1
        l_max: int = height[l]
        r_max: int = height[r]
        water: int = 0
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(height[l], l_max)
                water += l_max - height[l]
            else:
                r -= 1
                r_max = max(height[r], r_max)
                water += r_max - height[r]
        
        return water