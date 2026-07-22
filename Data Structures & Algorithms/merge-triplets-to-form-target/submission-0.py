class Solution:
    # Runtime: O(n)
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Which array is good to use
        good = set()

        for t in triplets:
            # If any of the triplet value is greater than the target, never use it
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            # i is position and v is value
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
            
        
        return len(good) == 3





        