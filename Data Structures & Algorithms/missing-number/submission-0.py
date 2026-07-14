class Solution:
    # Runtime: O(n)
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        for i in range(len(nums)):
            result += (i - nums[i]) # sum(i) - sum(nums) will give you the missing number
        
        return result


        