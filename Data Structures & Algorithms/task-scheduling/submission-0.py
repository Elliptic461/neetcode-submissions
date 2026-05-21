class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Use max heap to figure out which task is the most frequent one
        # Runtime: O(n)
        # Count each occurence of each character
        count = Counter(tasks)
        maxHeap = [cnt for cnt in count.values()]
        heapq.heapify_max(maxHeap)

        # Keep track of time
        time = 0
        q = deque() # pairs of [cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                # Process this task
                cnt = heapq.heappop_max(maxHeap) - 1
                if cnt:
                    q.append([cnt, time + n])
            
            # Time has been reached
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])
        
        return time






