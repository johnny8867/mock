# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        slow = head
        fast = head.next

        while fast:
            if slow.val == fast.val:
                fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next
        slow.next = fast
        return head
        #O(n), O(1)