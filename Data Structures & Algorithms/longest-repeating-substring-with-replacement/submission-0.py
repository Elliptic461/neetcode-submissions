class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        count = {}
        left = 0

        for r in range(len(s)):
            # Keep track of the frequency of the letter visited from the current 
            # sliding window
            count[s[r]] = 1 + count.get(s[r],0)

            # While current window size - largest frequent letter > k
            # Move the left pointer, since we are decreasing. Decrement that letter
            # from the hashmap table.
            while (r - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, r - left + 1)
        
        return result



