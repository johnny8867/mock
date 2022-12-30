# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = temp = head

        for _ in range(n):
            temp = temp.next

        if temp == None:
            return head.next

        while temp.next != None:
            temp = temp.next
            cur = cur.next
        cur.next = cur.next.next
        return head
        #O(n), O(1)