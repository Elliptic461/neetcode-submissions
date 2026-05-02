class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        result = float('infinity')

        # Perform binary search = O(log(n))
        while left <= right:
            mid = (left + right) // 2
            result = min(result, nums[mid])

            # If mid num greater than right num, than the min number
            # must be on the right side of the array, vice versa
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        return result
            