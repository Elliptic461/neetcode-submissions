"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # Runtime: O(nlog(n))
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Given some input, which I'll call i, hand back i.start. Then sort it by i.start
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        result, count = 0, 0
        sp, ep = 0, 0

        while sp < len(intervals):
            if start[sp] < end[ep]:
                sp += 1 # Another meeting has started
                count += 1
            else:
                ep += 1 # Meeting has ended
                count -= 1
            
            result = max(result, count)

        return result


        
        



        