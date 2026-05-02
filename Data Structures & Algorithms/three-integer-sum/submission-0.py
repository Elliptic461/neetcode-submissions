class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # Sorted = O(nlog(n))
        nums.sort()

        for i, n in enumerate(nums):
            # If the next number has been used before, skip it
            if i > 0 and n == nums[i - 1]:
                continue 

            # Setting up two pointers
            left = i + 1
            right = len(nums) - 1
            
            # Find every possible combination using two pointers 
            while left < right:
                # If sum greater than 0, move right. If sum < 0, move left
                if n + nums[left] + nums[right] > 0:
                    right -= 1
                elif n + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    # If sum = 0, add it to the result and move left pointer
                    result.append([n,nums[left],nums[right]])
                    left += 1
                    # There maybe duplicate for the next number, so check it as well
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        # O(n^2)
        return result

