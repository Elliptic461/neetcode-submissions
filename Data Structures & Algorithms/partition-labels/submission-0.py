class Solution:
    # runtime: O(n)
    def partitionLabels(self, s: str) -> List[int]:
        # Idea is to use hashmap and store the character and their last occurence
        lastIndex = {} # Char -> last index in s

        for i, c in enumerate(s):
            lastIndex[c] = i

        result = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            if lastIndex[c] > end:
                end = lastIndex[c]
            
            if i == end:
                result.append(size)
                size = 0

        return result





        