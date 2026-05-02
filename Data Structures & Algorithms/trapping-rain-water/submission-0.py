class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0

        # Keep track of the max left and max right
        left = 0
        right = len(height) - 1
        maxLeft = height[left] 
        maxRight = height[right]
        result = 0

        while left < right:
            # If current max left is < than current max right, move left pointer. 
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                result += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                result += maxRight - height[right]
        
        return result
