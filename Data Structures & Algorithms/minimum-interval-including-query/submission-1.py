class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []  # Contain (length of the interval, end value of this interval)
        result = {}  # Since we will be sorting queries, we need hashmap to keep track
        i = 0

        for q in sorted(queries):
            # Keep pushing intervals into the minHeap as long as we still have
            # intervals to push into the minHeap and the left value of the interval
            # is less than the current query value
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            # Pop interval from minHeap if the right value is less than the current query value
            # This mean this query value can never be apart of this interval
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            result[q] = minHeap[0][0] if minHeap else -1
        
        return [result[q] for q in queries]
