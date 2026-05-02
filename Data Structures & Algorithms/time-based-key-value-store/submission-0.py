class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list) # key = string, value = [list of [value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
            result = ""
            values = self.timeMap.get(key, [])

            # Binary search: O(log(n))
            left, right = 0, len(values) - 1
            while left <= right:
                mid = (left + right) // 2

                # If less than or equal to timestamp, then we are good
                if values[mid][1] <= timestamp:
                    result = values[mid][0] 
                    left = mid + 1
                else:
                    right = mid - 1
            
            # Runtime: O(log(n))
            return result


