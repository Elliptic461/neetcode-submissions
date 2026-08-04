class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" :  "["} 

        for c in s:
            # If this backet is a close backet
            if c in closeToOpen:
                # Make sure it is not empty and there is an open backet of that type.
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        
        return True
        




        
        