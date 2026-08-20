class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Each hashmap keep track of how many occurrences of letter in the string
        str1Hashmap = {}
        str2Hashmap = {}

        # Fill the hashmap
        for s in s:
            str1Hashmap[s] = 1 + str1Hashmap.get(s, 0)
        
        for t in t:
            str2Hashmap[t] = 1 + str2Hashmap.get(t, 0)
        
        
        if str1Hashmap == str2Hashmap:
            return True
        
        return False

