class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Creating an array of pairs [position, speed]
        pair = [[p,s] for p, s in zip(position, speed)]
        
        stack = []

        # Sorted, O(log(n))
        # Also going through the list: O(n)
        for p, s in sorted(pair)[::-1]: # Reverse sorted order
            # Calculate time and add it to the stack. 
            stack.append((target - p) / s)
            
            # If there is at least 2 cars in the stack and the top car is less than 
            # second to last car. Car fleet has occured
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        #Runtime: O(n*log(n))
        return len(stack)
