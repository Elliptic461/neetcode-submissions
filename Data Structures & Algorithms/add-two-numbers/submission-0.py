# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        # Carry is also part of condition because edge case where l1
        # and l2 reach the end of the list, but the last numbers result in a carry over
        # Thus, still need to add it to dummy
        while l1 or l2 or carry:
            # Grab the value
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry

            # Get carry over (when v1 + v2 = overflow)
            carry = val // 10
            val = val % 10

            curr.next = ListNode(val) 

            # Update curr
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        #Runtime: O(m + n)
        return dummy.next

            







