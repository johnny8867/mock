# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first = head
        second = self.get_middle(head)
        temp = second.next
        second.next = None

        second = temp

        left = self.sortList(first)
        right = self.sortList(second)
        return self.merge(left, right)

        
    def get_middle(self, head):
        slow = head
        fast = head.next ##not sure why this has to be head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        dummy = ListNode(0)
        result = dummy

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        dummy.next = list1 or list2

        return result.next