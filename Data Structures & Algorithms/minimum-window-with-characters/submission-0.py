class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}

        # Build the hashmap for t 
        for c in t:
            countT[c] = 1 + countT.get(c, 0) 

        have, need = 0, len(countT)
        result, resultLen = [-1, -1], float("infinity")
        left = 0

        for r in range(len(s)):
            # Build hashmap for current window
            c = s[r] 
            window[c] = 1 + window.get(c, 0)

            # If character in countT and satisfy condition in that 
            # key pair row 
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                #Update our result
                if (r - left + 1) < resultLen:
                    result = [left, r] 
                    resultLen = r - left + 1
                
                # Pop from the left of the window
                window[s[left]] -= 1
                # Checking if removing the character result in have not equal
                # to need
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        
        # Extract the substring
        left, r = result 

        return s[left: r + 1] if resultLen != float("infinity") else ""







