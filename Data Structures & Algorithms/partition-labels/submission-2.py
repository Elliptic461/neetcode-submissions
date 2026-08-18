class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i
        

        size = 0
        result = []
        end = 0

        for i, c in enumerate(s):
            size += 1

            if lastIndex[c] > end:
                end = lastIndex[c]
            
            if i == end:
                result.append(size)
                size = 0
        
        return result
            


        