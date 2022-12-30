# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        dummy = ListNode(0)
        dummy.next = head
        result = dummy

        for i in range(length - n):
            dummy = dummy.next

        dummy.next = dummy.next.next

        return result.next
        #O(2*N), O(N)