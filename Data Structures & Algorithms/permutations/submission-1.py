class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base case return empty array
        if len(nums) == 0:
            return [[]]
        
        # Create a subarray without the first element
        perms = self.permute(nums[1:])
        result = []

        # For every number in the subarray
        # 
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                result.append(p_copy)

        return result

        