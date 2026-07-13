class Solution:
    # Runtime: O(1)
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            # Pull the lowest bit off n, shift the result left to make room
            # and drop that bit in.
            result = (result << 1) | (n & 1)
            n = n >> 1
        
        return result