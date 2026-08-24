class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap that holds frequent array
        freq = [[] for i in range(len(nums) + 1)] # Bucket array, number with frequent i

        # Count how many each number has appear
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Number of occuerence (c) -> array of letter that appear c times
        for n, c in count.items():
            freq[c].append(n)
        
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)

                if len(result) == k:
                    return result
        

        