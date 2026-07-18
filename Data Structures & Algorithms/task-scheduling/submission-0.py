class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        max_heap = [-cnt for cnt in counts.values()]

        heapq.heapify(max_heap)

        time = 0
        q = []
        while max_heap or q:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt < 0:
                    q.append((time+n, cnt))
            
            if q and q[0][0] == time:
                heapq.heappush(max_heap, q.pop(0)[1])

        return time