class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Counting the number of times a number occurs. 
        for n in nums:
            count[n] = 1 + count.get(n,0)

        # key,value
        for n,c in count.items():
            freq[c].append(n) # This value n appear exactly c number of times.

        result = []

        # O(n) 
        for i in range(len(freq) - 1, 0, -1):
            # O(n) 
            for n in freq[i]:
                result.append(n)
                
                # Once hit k most frequent elements within the array. 
                if len(result) == k:
                    return result

        # Overall runtime: O(n)
        # Each elements appear in a bucket exactly once. So Worst case, you are collecting all the elements. Thus its O(n) times.



        