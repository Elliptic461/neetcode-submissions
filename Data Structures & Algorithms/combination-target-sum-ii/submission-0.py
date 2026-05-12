class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = [] 

        candidates.sort()

        # index use to keep track on what value we are allowed to use
        def dfs(index, curr, total):
            
            # Found target
            if total == target:
                result.append(curr.copy())
                return 
            
            if index >= len(candidates) or total > target:
                return
            
            # Include nums[index], this time must be index + 1 because we are not allowed to reuse the element
            curr.append(candidates[index])
            dfs(index + 1, curr, total + candidates[index])
            
            # Not allow to use nums[index]
            curr.pop()
            # If the next number is the same, skip it. This is possible because it is sorted
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1

            dfs(index + 1, curr, total)

        
        dfs(0, [], 0)
        return result