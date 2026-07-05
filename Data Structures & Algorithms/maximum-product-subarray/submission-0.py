class Solution:
    # Runtime: O(n)
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)  
        curMin, curMax = 1, 1

        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            result = max(result, curMax, curMin)
        
        return result

        