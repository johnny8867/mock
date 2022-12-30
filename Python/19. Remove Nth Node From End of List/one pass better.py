# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        result = dummy
        cur = head

        for i in range(n):
            cur = cur.next

        while cur != None:
            cur = cur.next
            dummy = dummy.next
        dummy.next = dummy.next.next

        return result.next
        #O(n), O(1)