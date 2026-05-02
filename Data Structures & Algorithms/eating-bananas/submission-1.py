class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # len(p) <= h
        
        left, right = 1, max(piles)
        result = right

        # Binary search for k is log(m)
        while left <= right:
            k = (left + right) // 2
            # Store how many hours does it take to eat all banana
            hours = 0 

            # Calculate the totals hours for current k found is O(n)
            for p in piles:
                hours += math.ceil(p / k)
            
            # If hours is less or equal to h 
            # Valid integer, so check if it is the minimum integer for now
            # Then move right to the middle.
            if hours <= h:
                result = min(result, k)
                right = k - 1
            else:
                left = k + 1
        
        # Runtime: O(n*log(m))
        return result


