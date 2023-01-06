import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        contain = []
        for node in lists:
            while node:
                heapq.heappush(contain, node.val)
                node = node.next

        cur = dummy = ListNode(0)

        while contain:
            dummy.next = ListNode(heapq.heappop(contain))
            dummy = dummy.next

        return cur.next
        #O(nlogn + n), O(n)