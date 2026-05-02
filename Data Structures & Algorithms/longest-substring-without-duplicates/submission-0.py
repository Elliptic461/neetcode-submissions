class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        result = 0

        # i will be my right pointer
        for i in range(len(s)):

            #If letter is already in set
            while s[i] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[i])
            result = max(result, i - left + 1)

        # Runtime: O(n)
        return result
            