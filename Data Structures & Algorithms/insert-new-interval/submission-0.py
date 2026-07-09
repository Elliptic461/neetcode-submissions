class Solution:
    # Runtime: O(n)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            # If the right most new interval value is less than 
            # the left most interval value, than all interval that comes after will not overlap
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            else: # Is overlapping
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        result.append(newInterval)
        return result
            


        
        