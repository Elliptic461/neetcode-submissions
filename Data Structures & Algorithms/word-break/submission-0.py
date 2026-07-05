class Solution:
    # Runtime: O(n^2 * m)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp =  [False] * (len(s) + 1)

        dp[len(s)] = True # Base case

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict: 
                # Checking if the current word is in dictionary
                if (i + len(w)) <= len(s) and s[i: i + len(w)] ==  w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]




        