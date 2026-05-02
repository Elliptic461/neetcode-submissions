class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # Pair: [index, height]

        for i, h in enumerate(heights):
            start = i # Use for extending it backward
            
            # If stack is not empty and top of the stack height is greater than 
            # the next height, pop the top the stack and calculate its area
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Check if the current height pop is greater than the current max area
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        # Some heights still exist in stack, calculate those areas as well
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        # Runtime: O(n)
        return maxArea
