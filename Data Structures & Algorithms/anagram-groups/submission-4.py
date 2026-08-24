class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use defaultdict because it creates a key if key does not exist
        # in the hashmap
        groupAna = defaultdict(list) # mapping character count to list of anagrams

        for s in strs:
            count = [0]*26 # Represent the alphabet count (a to z)

            for c in s:
                # Trick to convert lowercase letter to index for arrays
                count[ord(c) - ord('a')] += 1
            
            groupAna[tuple(count)].append(s)
        
        return list(groupAna.values())




        