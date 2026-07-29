class Solution:
    # O(m *n) where m is the length of s and n is the length of string t
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            
            if i == len(s):
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            # If character match, you can now skip it or use it. This is to cover the case like this: s = caaat, t= cat where you can use different "a"
            if s[i] == t[j]:
                dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else: # If character is not a match, you have to skip it
                dp[(i, j)] = dfs(i + 1, j)
            
            return dp[(i, j)]
        
        return dfs(0, 0)

        