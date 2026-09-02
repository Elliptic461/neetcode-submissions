class Solution:

    def encode(self, strs: List[str]) -> str:
        convert = ''

        # Idea is we append a number that represent the length of the string
        # and a # symbol to signal that the next character is the actually string.
        for i in strs:
            convert += str(len(i)) + '#' + i 
        
        return convert

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            
            # Find where # symbol is so we can grab the length
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            result.append(s[j + 1: length + j + 1])

            i = length + j + 1
        
        return result
            





