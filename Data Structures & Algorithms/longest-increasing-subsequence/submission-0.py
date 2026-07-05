class Solution:
    # Runtime: O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        #cache
        LIS = [1] * len(nums)

        # i represent the element that will be compare to other element
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                # Check if it is increasing order
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)

        





        