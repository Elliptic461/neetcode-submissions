class Solution:

    def encode(self, strs: List[str]) -> str:
        single = ""

        # Idea is that neet -> 4#neet
        # O(n) where n is the number of strings in the array
        for i in strs:
            convert = str(len(i)) + "#" + i
            single += convert
        return single

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            result.append(s[j + 1:length + j + 1])

            i = length + j + 1

        return result



        

