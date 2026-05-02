class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hash = {}
        for i in range(len(nums)):
            j = target - nums[i]

            if j in Hash:
                index = Hash[j]
                array = [index,i]
                return array
            else:
                Hash[nums[i]] = i 
            


        