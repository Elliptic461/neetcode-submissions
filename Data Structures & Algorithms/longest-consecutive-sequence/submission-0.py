class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Idea here is to find the start of the sequence
        # Hashset does not store value, only track unique keys
        numSet = set(nums)
        longest = 0

        for n in nums:
            # Check if start of a sequence
            if (n-1) not in numSet:
                length = 0
                
                # Check if there exist a n + 1, if there is, then check for n + 2 and so on.
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest

