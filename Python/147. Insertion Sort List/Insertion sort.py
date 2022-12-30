# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        
        while head:
            prev = dummy
            while prev.next and prev.next.val < head.val:
                prev = prev.next
            
            temp = head.next
            head.next = prev.next
            prev.next = head

            head = temp
        return dummy.next
        #O(n^2), O(n)