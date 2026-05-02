class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashs = {} 
        
        for i in range(len(nums)):
            find = target - nums[i]

            if find in hashs:
                return [hashs[find], i]
            else:
                hashs[nums[i]] = i

            