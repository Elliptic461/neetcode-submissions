class Solution:
    # Runtime: O(1) cause number is guarantee to be at most 32 iteration (32 bit)
    def hammingWeight(self, n: int) -> int:
        result = 0 

        while n:
            n &= n - 1
            result += 1

        return result
        


        