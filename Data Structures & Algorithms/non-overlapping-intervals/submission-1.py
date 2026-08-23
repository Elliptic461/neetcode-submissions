class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Need to sort it so we can compare intervals to each out
        intervals.sort()
        result = 0
        # Keep track of the end value
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # They are not overlapping
            if start >= prevEnd:
                prevEnd = end
            else:
                # Else they are overlapping 
                # Keep the end value that is smaller
                # Since that leaves more room for future interval to not overlap
                result += 1
                prevEnd = min(prevEnd, end)
        
        return result

                    






        