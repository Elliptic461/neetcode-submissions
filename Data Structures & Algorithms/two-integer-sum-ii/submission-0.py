class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        result = []
        
        while left < right:
            # If two number added is greater than target, decrease right. 
            # If two number added is less than target, increase left.
            # If two number added are equal, return the indices
            if numbers[left] + numbers[right] == target:
                result.append(left + 1)
                result.append(right + 1)
                return result
            elif numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            

