"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        stk = []
        intervals.sort(key=lambda x: (x.start))
        for i in intervals:
            if stk and i.start < stk[-1].end:
                return False
            
            stk.append(i)
        
        return True
