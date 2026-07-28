class Solution:
    # Runtime: O(m * n)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = []
        # Iterate per row
        for i in range(len(s1) + 1):
            newRow = []
            # Iterate per column
            for j in range(len(s2) + 1):
                newRow.append(False)
            dp.append(newRow)

        # Enable corner value as True
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True

                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]
