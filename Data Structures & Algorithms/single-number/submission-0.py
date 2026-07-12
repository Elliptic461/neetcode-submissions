class Solution:
    # Runtime: O(n)
    def singleNumber(self, nums: List[int]) -> int:
        # Solve using bit manipulation, use XOR. 
        # We know that a ^ a = 0 and a ^ 0 = a
        # If you XOR every element together, each pair cancel itself to 0
        # except for the lone number, which survives.

        result = 0
        for n in nums:
            result ^= n
        
        return result

        