# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy

        while dummy and dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        return cur.next
        #O(n), O(n)