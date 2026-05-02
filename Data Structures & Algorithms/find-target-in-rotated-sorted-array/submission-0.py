class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # Perform binary search, O(log(n))
        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            
            # If mid num is part of the left portion:
            # left side is ascending order
            if nums[left] <= nums[mid]:
                # If target greater than mid num, search right side
                # Same if target greater than left num
                # Ex: target = 7. array = 4,5,6,7,0,1,2
                # if mid is 6, we know we need to search right portion
                # Another check is if the far left number is greater than
                # target, than we know we need to search right
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # search right portion 
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        # Runtime: O(log(n))
        return -1
