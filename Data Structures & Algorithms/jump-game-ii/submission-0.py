class Solution:
    # Runtime: O(n)
    def jump(self, nums: List[int]) -> int:
        result = 0 
        # Represent window from index 0 to index 0
        # Determine what portion of the array is use for bfs
        l, r = 0, 0

        while r < len(nums) - 1:
            farthest = 0
            # i tells us the max distance we can jump
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest
            result += 1
        
        return result

        