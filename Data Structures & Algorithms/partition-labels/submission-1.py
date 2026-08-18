class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # char -> last index in s
        lastIndex = {} 

        # Fill the hashmap
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        result = []
        # end represent the index of where the last character 
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1

            if lastIndex[c] > end:
                end = lastIndex[c]
            
            # If index reach the end of a last character
            # which means next character is a new character that we have not seen before yet
            # So split the current string into a substring
            if i == end:
                result.append(size)
                size = 0 
    
        return result








        
        