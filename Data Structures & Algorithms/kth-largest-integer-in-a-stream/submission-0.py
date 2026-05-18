class KthLargest:
    # Use min heap of size k
    # runtime: nlog(n)
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        # Creating the min heap and pop until equal to k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        # Edge case where number of element is less than k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]
