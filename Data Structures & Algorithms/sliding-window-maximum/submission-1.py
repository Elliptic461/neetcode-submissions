class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = 0
        right = 0
        # We use a deque to always drop the lowest number and keep the highest
        deque = collections.deque()


        while right < len(nums):
            # If a value at the back of the deque is smaller than the incoming value,
            # it can never be the max again (the new value is both bigger and will
            # outlast it in the window), so remove it. This keeps the deque's values
            # in strictly decreasing order from front to back.
            while deque and nums[deque[-1]] < nums[right]:
                deque.pop()
            
            deque.append(right)

            # if left 
            if left > deque[0]:
                deque.popleft()
            
            # Shift the right pointer
            if (right + 1) >= k:
                result.append(nums[deque[0]])
                left += 1
            
            right += 1
        
        return result





        
        