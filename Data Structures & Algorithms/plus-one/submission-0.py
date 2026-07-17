class Solution:
    # Runtime: O(n)
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one, i = 1, 0

        while one:
            # Within bounds
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    one = 0
            else: # Out of bound
                digits.append(1)
                one = 0
            i += 1
        
        return digits[::-1]

        