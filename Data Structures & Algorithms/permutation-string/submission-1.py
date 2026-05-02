class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0]*26, [0]*26

        # Add the letter from the first string and some of the letters from the 
        # second string to the array
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # This part if s1 is apart of s2 in the first part of the second string
        # O(26)
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        # O(n)
        left = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # Find the index position of that letter and increment it in s2Count array
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            # If there equal, then a match has been found. 
            # Else, if that increment made it unequal, we have to decrement count
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Since we increment right, we also need to increment left
            # And calculate its index position 
            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1

            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            left += 1
        
        # Runtime: O(n)
        return matches == 26

            
            

        


