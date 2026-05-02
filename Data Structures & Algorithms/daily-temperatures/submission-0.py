class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [temp, index]
        result = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            # Check if stack is empty and if top of the stack less than current temp
            while stack and t > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                result[stackIdx] = i - stackIdx
            stack.append([t, i])
        return result


                