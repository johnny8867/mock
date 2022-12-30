# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        List = head
        count = 0
        while head:
            count += 1
            head = head.next
        
        mid = count // 2

        if count == 1:
            return List
        while mid:
            mid -= 1
            List = List.next
        
        return List
        #O(n), O(1)