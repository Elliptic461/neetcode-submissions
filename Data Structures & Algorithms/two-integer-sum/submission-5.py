class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            j = target - nums[i]

            if j in hashmap:
                return [hashmap[j], i]
            
            hashmap[nums[i]] = i 
        