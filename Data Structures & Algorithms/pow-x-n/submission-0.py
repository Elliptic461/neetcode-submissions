class Solution:
    #Runtime: O(log(n))
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0

            if n == 0:
                return 1
            
            result = helper(x, n // 2)
            result = result * result
            # If n is an odd number, else its even so return result
            return result * x if n % 2  else result

        result = helper(x, abs(n))
        
        # Check if input n is negative
        return result if n >= 0 else 1 / result
        


        