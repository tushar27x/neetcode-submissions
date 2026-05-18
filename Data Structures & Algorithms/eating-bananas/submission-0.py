class Solution:
    def get_hours(self, m: int, piles: List[int]) -> int:
        ans = 0
        for p in piles:
            ans += math.ceil(p / m)
        
        return ans

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 0
        while l <= r:
            m = l + (r-l) // 2
            hours = self.get_hours(m, piles)

            if hours <= h:
                ans = m
                r = m-1
            else:
                l = m+1
        
        return ans