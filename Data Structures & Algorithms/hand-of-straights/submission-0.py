class Solution:
    # Runtime: O(nlog(n))
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        # Get the count of the cards
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first + groupSize):
                # Check if i is avaiable to us
                if i not in count:
                    return False
                
                count[i] -= 1

                # Check if this number reached 0, if so we will have to pop it
                if count[i] == 0:
                    # If this is not the minimum value we are trying to pop
                    if i != minHeap[0]:
                        return False
                    
                    heapq.heappop(minHeap)
        
        return True



        