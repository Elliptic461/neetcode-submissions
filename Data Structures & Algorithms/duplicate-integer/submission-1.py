class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        
        for i in nums:
            if i in hashmap:
                return True
            else:
                hashmap[i] = 0 
        return False