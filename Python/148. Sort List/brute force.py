# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hold = []
        dummy = ListNode(0)
        dummy.next = head

        while dummy.next:
            dummy = dummy.next
            hold.append(dummy.val)

        new_head = ListNode(0)
        result = new_head

        hold.sort()

        for item in hold:
            new = ListNode(item)
            new_head.next = new
            new_head = new_head.next

        return result.next
        #(NlogN), O(N)