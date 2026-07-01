class Solution:
    # Runtime: O(n)
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1} # key value pair: len(s) -> 1

        # Start in reverse order
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else: # Its a digit 1-9
                dp[i] = dp[i + 1] # inherit the count from the next index
            
            # Checking if i is not at the end of len(s) and if the current ith digit is 1 or 2 where 2 must have a digit 1-6 follow after
            if (i + 1 < len(s) and (s[i] == "1" or 
                    s[i] == "2" and s[i + 1] in "0123456")):
                    dp[i] += dp[i + 2]
        
        return dp[0]


        