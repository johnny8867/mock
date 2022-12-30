# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        PA = headA
        PB = headB

        while PA != PB:
            PA = PA.next if PA else headB
            PB = PB.next if PB else headA
        return PA
        #O(N), O(1)