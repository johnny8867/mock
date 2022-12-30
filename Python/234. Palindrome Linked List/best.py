# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow: #reverse half to end -> end to half
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        cur = head

        while prev:
            if prev.val != cur.val:
                return False
            prev = prev.next
            cur = cur.next
        return True
        #O(n), O(1)