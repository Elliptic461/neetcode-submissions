class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Hashmap = {} 

        for i in range(len(strs)):
            array = [0 for i in range(26)]
            word = strs[i]

            for j in word:
                array[ord(j) - ord('a')] += 1
            
            tuples = tuple(array)

            if tuples in Hashmap:
                Hashmap[tuples].append(word)
            else:
                Hashmap[tuples] = [word]
        
        return list(Hashmap.values())



            
