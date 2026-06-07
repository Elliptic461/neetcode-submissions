class Solution:
    # Runtime: O(n*m^2)
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Build adjacency list
        # Run BFS to find shortest path

        if endWord not in wordList:
            return 0 
        
        # List of neighbor (adjacency list)
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        # Find all pattern of this word
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])
        result = 1 
        
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return result
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
                
            result += 1

        return 0




