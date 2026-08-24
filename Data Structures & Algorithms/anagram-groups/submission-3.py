class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAna = {} # key (sorted) -> array of the same anagram

        for c in strs:
            key = "".join(sorted(c))

            if key in groupAna:
                groupAna[key].append(c)
            else:
                groupAna[key] = [c]
        

        result = []
        for key in groupAna:
            result.append(groupAna[key])
        

        return result


        