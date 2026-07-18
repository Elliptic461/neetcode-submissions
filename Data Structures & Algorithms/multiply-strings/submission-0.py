class Solution:
    # Runtime: O(m*n) where m is the length of the string num1 and n is the length of string num2 
    def multiply(self, num1: str, num2: str) -> str:
        # If any of the string is just 0
        if "0" in [num1, num2]:
            return "0"
        
        result = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                # Store digit at this position, also adding cause there might be a number 
                # already at this position
                result[i1 + i2] += digit

                # Put the carry value here
                result[i1 + i2 + 1] += (result[i1 + i2] // 10)

                result[i1 + i2] = result[i1 + i2] % 10
        
        result, begin = result[::-1], 0

        # While begin is not out of bound and there is still leading zeros
        while begin < len(result) and result[begin] == 0:
            begin += 1
        
        result = map(str, result[begin:])
        return "".join(result)




        