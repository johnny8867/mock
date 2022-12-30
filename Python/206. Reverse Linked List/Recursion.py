# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = self.reverseList(head.next)
        head.next.next = head # 4 -> 5 = 4.next.next = head -> 5.next = 4
        head.next = None #make the head point to null
        
        return prev #return to call stack
    
    #O(n), O(n)