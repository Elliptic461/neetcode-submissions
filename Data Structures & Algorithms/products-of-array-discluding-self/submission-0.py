class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1]
        prefix = 1
        postfix = 1

        # Calculating prefix
        for i in range(len(nums) - 1):
            output.append(nums[i] * prefix)
            prefix = nums[i] * prefix

        # Calculating postfix
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * postfix
            postfix = nums[i] * postfix
            

        return output