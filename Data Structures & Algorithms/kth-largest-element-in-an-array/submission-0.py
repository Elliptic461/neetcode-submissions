class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use max heap
        # runtime: n + klog(n)
        heapq.heapify_max(nums)

        for i in range(k - 1):
            heapq.heappop_max(nums)
        return heapq.heappop_max(nums)



        