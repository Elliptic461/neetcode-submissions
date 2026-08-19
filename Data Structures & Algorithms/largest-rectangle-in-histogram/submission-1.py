class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        # pair: (index, height)
        stack = [] 

        for i,h in enumerate(heights):
            start = i

            # If stack is not empty and top of the stack height is greater than 
            # the next height, pop the top the stack and calculate its area
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                # The popped bar was taller than h, so a rectangle of height h
                # could have started as far back as that bar did too.
                # Carry its index forward as our new leftmost boundary.
                start = index
            stack.append((start, h))
        
        # Some heights still exist in stack, calculate those areas as well
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea
        