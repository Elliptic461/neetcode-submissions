class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def addWord(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Use trie data structure
        root = TrieNode()

        for w in words:
            root.addWord(w)
        
        rows, cols = len(board), len(board[0])
        result, visit = set(), set()

        def dfs(r, c, currNode, word):
            if (r < 0 or c < 0 or r == rows or c == cols or
                    (r,c) in visit or board[r][c] not in currNode.children):
                    return 
            
            # Can't visit the same cell twice
            visit.add((r,c))
            currNode = currNode.children[board[r][c]]
            word += board[r][c]
            if currNode.endOfWord:
                result.add(word)
            
            dfs(r - 1,c, currNode, word)
            dfs(r + 1,c, currNode, word)
            dfs(r,c - 1, currNode, word)
            dfs(r,c + 1, currNode, word)
            visit.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
            
        return list(result)









    