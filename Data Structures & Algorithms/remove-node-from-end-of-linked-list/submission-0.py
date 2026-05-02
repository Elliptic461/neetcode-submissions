# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            prev = prev.next
            right = right.next
        
        #delete node
        prev.next = prev.next.next

        # Runtime: O(N)
        return dummy.next
        
        

        

        

        
