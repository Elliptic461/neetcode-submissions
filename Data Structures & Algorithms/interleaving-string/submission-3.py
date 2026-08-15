class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = []

        # Building the 2-D Array
        for i in range(len(s1) + 1):
            newRow = []
            for j in range(len(s2) + 1):
                newRow.append(False)
            dp.append(newRow)
        
        # Enable corner value as True, represent that both string as being used up
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # Try taking the next s3 char from s1:
                # s1 still has chars left (i in bounds), s1[i] matches the
                # current s3 char (position i+j = total chars remaining),
                # and the rest interleaves after using s1[i] -> dp[i+1][j]
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                
                # Try taking the next s3 char from s2 instead:
                # same idea, advancing j and checking dp[i][j+1]
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]





        

        