class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0 

        while left != right:
            # Calculate current area, height is bottleneck by small height
            currArea = min(heights[left],heights[right]) * (right - left)
            maxArea = max(currArea, maxArea)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        # Runtime: O(n)
        return maxArea


