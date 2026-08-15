class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root

        for s in word:
            if s not in cur.children:
                cur.children[s] = TrieNode()
            cur = cur.children[s]
        
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for s in word:
            if s not in cur.children:
                return False
            cur = cur.children[s]
        
        return cur.endOfWord
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for s in prefix:
            if s not in cur.children:
                return False
            cur = cur.children[s]
        
        return True
        
        