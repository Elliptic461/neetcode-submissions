class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = 0 
        right = 0
        dq = collections.deque() # Contain index

        while right < len(nums):
            # While queue is not empty and the number inside deqeue
            # is less than the current number, pop it (right side).
            # Ex: Given 1,1,1,1,1,4,5, k = 6
            # [1,1,1,1,1], add 4, remove all 1
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
            dq.append(right)

            # If left value is out of bound (After moving slider)
            if left > dq[0]:
                dq.popleft()
            
            if (right + 1) >= k:
                # Guarantee that right side is the largest number
                result.append(nums[dq[0]])
                left += 1
            right += 1
        
        # Runtime: O(n)
        return result

            