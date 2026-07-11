class Solution:
    # Runtime: O(nlog(n) + mLog(m)) where m is the size of array queries and n is the size of the array intervals
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        result, i = {}, 0

        for q in sorted(queries):
            # Check if i is less than the length of the interval array and that the ith interval start value
            # is less than the current query value
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                # Use right most value for tiebreaker and for removing interval where their end value
                # is less than the current query value
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            
            while minHeap and minHeap[0][1] < q:
                # Pop interval that are too far to the left
                heapq.heappop(minHeap)

            result[q] = minHeap[0][0] if minHeap else -1
        
        return [result[q] for q in queries]






        