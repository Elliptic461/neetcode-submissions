class Solution:
    # Runtime: O(nlog(n))
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        result = 0
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]:
            # Not overlapping
            if start >= prevEnd:
                prevEnd = end
            else: # Is overlapping
                result += 1
                prevEnd = min(prevEnd, end)
        
        return result




        