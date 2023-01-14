# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = head

        for i in range(k):
            if not tail:
                return head
            tail = tail.next
        new_head = self.reverse(head, tail)
        head.next = self.reverseKGroup(tail, k)
        return new_head

    def reverse(self, head, tail):
        prev = None
        while head != tail:
            head.next, prev, head = prev, head, head.next
        return prev
    #O(N), O(K)