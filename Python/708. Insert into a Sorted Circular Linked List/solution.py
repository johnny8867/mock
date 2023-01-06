"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        prev = head
        cur = head.next

        while prev.next != head:
            if prev.val <= insertVal <= cur.val:
                break
            elif prev.val > cur.val:
                if prev.val <= insertVal or insertVal <= cur.val: #at this point prev is the highest pt, cur is the lowest pt
                    break
            prev = prev.next
            cur = cur.next
        prev.next = Node(insertVal, cur)
        return head
        #O(n), O(1)