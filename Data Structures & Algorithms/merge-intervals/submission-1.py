class Solution:
    # Runtime: O(nlog(n)) 
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the interval by the start value of each interval
        intervals.sort()
        output = [intervals[0]]

        for start, end in intervals[1: ]:
            # Get most recently added interval, 2nd value to see if it overlap
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end) #Ex: [1, 5], [2, 4]
            else:
                output.append([start, end]) # Ex: [1,5], [7,8]
            
        
        return output




        