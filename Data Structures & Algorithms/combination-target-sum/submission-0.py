class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = [] 

        # index use to keep track on what value we are allowed to use
        def dfs(index, curr, total):
            if total == target:
                result.append(curr.copy())
                return 
            
            if index >= len(nums) or total > target:
                return
            
            # Include nums[index]
            curr.append(nums[index])
            dfs(index, curr, total + nums[index])

            # Not allow to use nums[index]
            curr.pop()
            dfs(index + 1, curr, total)
        

        dfs(0, [], 0)
        return result
            
