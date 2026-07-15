class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for n in stones:
            heapq.heappush(max_heap, -n)
        
        def smash():
            if len(max_heap) < 2:
                return
            
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)

            diff = abs(stone2 - stone1)

            heapq.heappush(max_heap, -diff)
            smash()
        
        smash()
        return -max_heap[0]