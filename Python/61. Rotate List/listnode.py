# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = head
        length = 1

        while dummy.next:
            length += 1
            dummy = dummy.next
        dummy.next = head

        for i in range(length - (k%length)):
            dummy = dummy.next

        result = dummy.next #this assign result
        dummy.next = None #this cut off tail
        
        return result
        #O(n), O(1)