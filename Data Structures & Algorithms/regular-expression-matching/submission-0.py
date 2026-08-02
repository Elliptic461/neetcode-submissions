class Solution:
    # Runtime: O(m *n)
    def isMatch(self, s: str, p: str) -> bool:
        # Top-down memoization

        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            if i >= len(s) and j >= len(p):
                return True

            # If only j is out of bound, then you can't try to match string s anymore.
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j + 1] == "*":
                dp[(i, j)] = (dfs(i, j + 2) or (match and dfs(i + 1, j))) # We don't use * or if char is a match, we can try to use *
                return dp[(i, j)]

            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]
            
            return False

        return dfs(0, 0)
