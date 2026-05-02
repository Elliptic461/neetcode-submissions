class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {'+', '-', '*', '/'}

        for t in tokens:

            if t not in operator:
                stack.append(t)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                
                if t == '+':
                    stack.append(num1 + num2) 
                elif t == '-':
                    stack.append(num2 - num1)
                elif t == '*':
                    stack.append(num1 * num2) 
                else:
                    stack.append(int(num2 / num1))
        
        return int(stack[0])