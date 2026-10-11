class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        res.append(intervals[0])
        for i in range(1, len(intervals)):
            prev = res[-1]
            curr = intervals[i]
            if curr[0] > prev[1]:
                res.append(curr)
            else:
                res[-1] = [min(prev[0], curr[0]), max(prev[1], curr[1])]
        
        return res