class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashs = defaultdict(list) # mapping charcount to list of Anagrams
        
        for s in strs:
            count = [0]*26 # a...z

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # In python, list can not be key. So turn into tuple since its non mutable
            hashs[tuple(count)].append(s) # Group the anagram of count, use defaultdict(list) if count doesn't exist case.
            

        return list(hashs.values())

            