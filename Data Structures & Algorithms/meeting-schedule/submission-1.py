"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # Runtime: O(nlog(n)) 
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Given some input, which I'll call i, hand back i.start. Then sort it by i.start
        intervals.sort(key = lambda i : i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        
        return True

