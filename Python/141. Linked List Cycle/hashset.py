# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        contain = set()

        while head:
            if head in contain:
                return True
            else:
                contain.add(head)
            head = head.next
        return False
        #O(n), O(n)