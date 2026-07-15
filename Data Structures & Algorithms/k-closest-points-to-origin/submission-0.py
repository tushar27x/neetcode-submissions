class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_from_origin = []
        for p in points:
            x = p[0]
            y = p[1]

            dist = math.sqrt((x**2) + (y**2))
            heapq.heappush(dist_from_origin, (-dist,p))
            if len(dist_from_origin) > k:
                heapq.heappop(dist_from_origin)
        
        ans = [p[1] for p in dist_from_origin]
        return ans