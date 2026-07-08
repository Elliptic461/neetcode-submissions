class Solution:
    # Runtime: O(N + V + E)
    def foreignDictionary(self, words: List[str]) -> str:
        # For every word in "words", for every character in each word
        adj = {c : set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            
            # Checking if a is a prefix of b and a.length < b.length
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            # Grab character from word
            for j in range(minLen):
                # If character are the same
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} # False = visited, True = visited and in current path
        result = []

        # c represent current character
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            # Go through neigbor of c
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            result.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        result.reverse()
        return "".join(result)




        