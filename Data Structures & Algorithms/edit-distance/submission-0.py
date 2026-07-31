class Solution:
    # Runtime: O(m * n)
    def minDistance(self, word1: str, word2: str) -> int:
        dp = []
        # Initialize dp
        for i in range(len(word1) + 1):
            newRow = []
            for j in range(len(word2) + 1):
                newRow.append(float("inf"))
            dp.append(newRow)
        
        # Initialize dp
        for w2 in range(len(word2) + 1):
            dp[len(word1)][w2] = len(word2) - w2
        
        for w1 in range(len(word1) + 1):
            dp[w1][len(word2)] = len(word1) - w1
        
        
        # Perform operation
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) -1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j+ 1], dp[i + 1][j], dp[i + 1][j+ 1])
        
        return dp[0][0]
        

            