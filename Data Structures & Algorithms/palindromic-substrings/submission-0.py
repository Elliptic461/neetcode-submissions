class Solution:
    # Runtime: O(n^2)
    def countSubstrings(self, s: str) -> int:
        result = 0 

        for i in range(len(s)):
            l, r = i, i
            result += self.countPali(s, l, r)

            l, r = i, i + 1
            result += self.countPali(s, l, r)
        
        return result
    
    def countPali(self, s, l, r):
        result = 0
        while l >=0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
        
        return result
        