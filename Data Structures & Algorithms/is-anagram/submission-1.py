class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        if len(s) != len(t):
            return False
        
        for i in s:
            if i not in hash1: # O(n)
                hash1[i] = 0
            else:
                hash1[i] += 1
    
        for j in t:
            if j not in hash2: # O(n)
                hash2[j] = 0
            else:
                hash2[j] += 1
        
        return hash1 == hash2 # Overall runtime O(n)
            