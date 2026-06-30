class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resultLen = 0

        def checkPalindromic(l: int,  r: int):
            # Tell python to reuse the one from the enclosing function's scope.
            nonlocal result, resultLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # Checking if the current length is longer than the length 
                # store in resultLen
                if (r - l + 1) > resultLen:
                    result = s[l:r+1]
                    resultLen = r - l + 1
                l -= 1
                r += 1

        for i in range(len(s)):
            # odd length
            l, r = i, i
            checkPalindromic(l, r)
            
            # even length
            l, r = i, i + 1
            checkPalindromic(l, r)
        return result

        

