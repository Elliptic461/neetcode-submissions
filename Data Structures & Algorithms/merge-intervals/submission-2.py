class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]


        for start, end in intervals[1:]:
            lastEnd = result[-1][1] 

            # If the start is within the interval, it is overlapping
            # So we merge them. Else, just add the interval
            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])


        return result

