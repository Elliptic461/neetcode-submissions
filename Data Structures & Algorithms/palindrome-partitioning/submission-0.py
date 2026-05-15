class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []

        def dfs(index):
            if index >= len(s):
                result.append(partition.copy())
                return
            
            # Generate every single possible substring
            # and check if its a palindrome
            for j in range(index, len(s)):
                if self.isPali(s, index, j):
                    partition.append(s[index:j + 1])
                    dfs(j + 1)
                    # Clean up
                    partition.pop()
        
        dfs(0)
        return result
    
    def isPali(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1
        
        return True
            
