# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0)
        dummy = result
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            to_add = (val1+val2+carry) % 10
            carry = (val1+val2+carry) // 10

            dummy.next = ListNode(to_add)
            dummy = dummy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            dummy.next = ListNode(carry)

        return result.next
        #O(max(l1, l2)), O(max(l1,l2)+1)
