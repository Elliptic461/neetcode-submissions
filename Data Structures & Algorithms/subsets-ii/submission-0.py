class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(index, subset):
            if index == len(nums):
                result.append(subset.copy()) 
                return
            
            # All subsets that include nums[i]
            subset.append(nums[index]) 
            backtrack(index + 1, subset)

            subset.pop()

            # All subset that don't include nums[i]
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            backtrack(index + 1, subset)
        

        backtrack(0, [])
        return result