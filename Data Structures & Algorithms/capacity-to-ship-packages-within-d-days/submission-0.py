class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(m):
            ships, cap = 1, m
            for w in weights:
                if cap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    cap = m
                
                cap -= w

            return True
        
        l, r = max(weights), sum(weights)
        ans = r
        while l<=r:
            m = l + ((r-l) // 2)
            if can_ship(m):
                ans = min(m, ans)
                r = m-1
            else:
                l = m+1
        
        return ans