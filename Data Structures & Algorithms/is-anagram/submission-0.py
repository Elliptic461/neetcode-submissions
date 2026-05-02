class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Hashmap = {} #character as key, value should be the counter
        Hashmap2 = {}
        for i in s:
            if i in Hashmap:
                Hashmap[i] = 1 + Hashmap[i]
            else:
                Hashmap[i] = 1
        
        for c in t:
            if c in Hashmap2:
                Hashmap2[c] = 1 + Hashmap2[c]
            else:
                Hashmap2[c] = 1
        return Hashmap == Hashmap2


                